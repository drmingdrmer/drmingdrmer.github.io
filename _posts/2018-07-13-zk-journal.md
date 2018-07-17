---
layout:     post
title:      "zk消息"
date:       2018 Jul 13
categories: tech architecture
tags:       tech architecture zookeeper journal subscribe
---

<!-- mdtoc start -->


<!-- mdtoc end   -->



<a class="md-anchor" name="the-big-picture"></a>

# The big picture

```
  human
    |
    |
    v
zookeeper                                    | Center IDC
  | | |
  | | |
  | | |
  | | `--> subscriber-1 ---+---------> nginx | edge IDC-1
  | |      subscriber-2    +---------> squid |
  | |                      `---------> squid |
  | |
  | `----> subscriber-1 ---+---------> nginx | edge IDC-2
  |        subscriber-2    +---------> squid |
  |                        `---------> squid |
  |
  +...
```



<a class="md-anchor" name="配置存储中心-zookeeper"></a>

# 配置存储中心: zookeeper

zookeeper 作为客户自定义配置的存储中心, 提供:

-   事务性更新操作(原子更新多个配置)
-   变更队列: 利用sequence节点, 实现一个让每个节点可以增量更新配置变化的队列.
-   同时也提供一个全量下载全部配置的接口.

zk中的存储按照域名(客户)来划分目录:

```
/record/com/
           `bsc/
               `img: {foo: bar...}
           `tencent/
               `www: {xxx: yyy...}
/tx/
    `journal/
        0000000001: ...
```



<a class="md-anchor" name="同类软件对比"></a>

## 同类软件对比

选择zk主要是由以下几个点, 跟其他几个软件对比的考虑:

|          | zk                       | etcd                                      | mysql                               |
| :--      | :--                      | :--                                       | :--                                 |
| 稳定性   | OK                       | 接口还在变                                | OK                                  |
| 运维简单 | 脚本化管理, 成员变更方便 | 困难:基于接口的操作方便人使用但自动化困难 | 困难:db/table初始化, 数据迁移等问题 |
| 事务性   | 强                       | 强                                        | 跨机房的部署缺少强一致性保证        |
| 权限控制 | 强                       | 一般                                      | 强                                  |
| 事件队列 | OK                       | OK                                        | 基于binlog, 不容易解析              |
| SDK      | 成熟, 多语言;            | 成熟, 多语言; shell脚本使用方便           | 成熟, 多语言                        |



<a class="md-anchor" name="事务性更新"></a>

# 事务性更新

管理员(human) 负责向zk提交配置变更, 提交变更的流程:

启动一个事务, 例如变更配置`img.bsc.com`的 `foo` 为 `wow`,
将`com/bsc/img` 的更新后的值 `{foo: wow}` 写入:

-   `/com/bsc/img` 这个节点; 用于全量更新

-   同时也在`/tx/journal`中追加一条记录如`0000000002`,
    记录修改的内容`{foo: wow}`, 用于增量更新.

事务提交后保证`com/bsc/img`和`tx/journal/0000000002`的变更同时出现.



<a class="md-anchor" name="journal订阅和更新"></a>

# Journal订阅和更新

`subscriber` 部署在每个IDC中, 负责将zk中的配置变更同步到机房内的每个需要的程序.

-   `subscriber` 至少有2个进程实例, 保证HA.

    由于对配置消费进程如nginx/squid的更新是指定版本号的(txid),
    所以可以保证2个`subscriber`进程即使同时运行也不会造成数据不一致.

    生成环境的部署应该尽可能保证同时只有1个`subscriber`在运行,
    这可以通过一个zk总的ephemeral node来实现互斥.

-   `subscriber`的工作流程是:

    -   启动, 检查它负责的程序nginx或squid是否有最后更新的journal的记录:
        -   如果有, 则开始增量更新, 从zk中拉取不存在的journal, 更新到nginx或squid里.
        -   如果没有, 则开始全量更新, 从zk中拉取所有的`record/`目录下的内容更新到nginx或squid.

    -   启动一个watcher线程, 监视zk变化, 如果有变化,
        例如`tx/journal/0000000002`被commit了, 则进行一次增量更新,
        提交`tx/journal/0000000002`中的修改到nginx和squid中.



<a class="md-anchor" name="配置消费进程-nginx-和-squid"></a>

# 配置消费进程 nginx 和 squid

nginx 或 squid 提供配置更新接口:

-   apply-conf: 用于更新一条配置, 参数:
    -   txid: 如`0000000002`, 用于确认新旧配置, 防止重复调用时旧配置覆盖新配置.
    -   data: 如`{foo: wow}`, 描述具体配置信息.

-   set-committed: 在内存中记录已经更新的事务id(txid)有哪些. 参数:
    -   data: `{...}`

-   get-committed: 读取在内存中记录已经更新的事务id(txid)有哪些. 没有参数, 返回:
    -   data: `{...}`

    这个接口被subscriber调用, 用来确定增量更新由哪开始继续.


<a class="md-anchor" name="问题"></a>

# 问题:


<a class="md-anchor" name="灰度发布"></a>

## 灰度发布

`subscriber` 需要有1个配置标识自己在第几个灰度级别:

-   立即: 占全网1%: 收到配置变化立即应用到ngnx/squid

-   10分钟: 占全网5%: 收到配置变化后等待5分钟应用到nginx/squid.
    这期间管理员可能再下发一个取消变更的事务到zk中,
    这时5分钟后`subscriber`发现被取消, 就不再更新.

-   30分钟: 类似..



<a class="md-anchor" name="网络隔离问题"></a>

## 网络隔离问题

如果有机房不能直接建立连接到zk, 可以有2个选择:

- 在中继机房建立zk代理(zk的一个slave节点), 如果这个可行的话, 架构简单一点.

- 或使用tcp代理(我还不太确定宏飞说的这个具体怎么实现的)



<a class="md-anchor" name="配置的持久化"></a>

## 配置的持久化

理论上subscriber 可以实现增量更新和全量更新, 因此不需要 nginx/squid持久化.

如果为了减少全量更新配置给中心zk带来的压力,
subscriber可以考虑负责缓存一个全部配置的snapshot.



<a class="md-anchor" name="配置消费进程的修改"></a>

## 配置消费进程的修改

这部分可能是最耗时的,
需要把nginx配置转换成通过lua解释配置信息来完成一个业务逻辑的形式.



<a class="md-anchor" name="建议-分区域"></a>

## 建议: 分区域

单中心的配置管理对全网服务更新有风险, 至少应拆分成一个测试环境(配置中心和测试用的节点)
和n个线上环境(配置中心和线上节点).


