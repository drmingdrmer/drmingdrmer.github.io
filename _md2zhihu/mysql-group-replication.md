
<!-- mdtoc start -->

-   [依赖: group-replication 需要gtid支持,多主复制基于gtid格式的binlog](%7B%7Bpage.url%7D%7D#%E4%BE%9D%E8%B5%96-group-replication-%E9%9C%80%E8%A6%81gtid%E6%94%AF%E6%8C%81%E5%A4%9A%E4%B8%BB%E5%A4%8D%E5%88%B6%E5%9F%BA%E4%BA%8Egtid%E6%A0%BC%E5%BC%8F%E7%9A%84binlog)
-   [特性: 多主模式:](%7B%7Bpage.url%7D%7D#%E7%89%B9%E6%80%A7-%E5%A4%9A%E4%B8%BB%E6%A8%A1%E5%BC%8F)
-   [限制: group-replication 只适合单机房高速局域网部署](%7B%7Bpage.url%7D%7D#%E9%99%90%E5%88%B6-group-replication-%E5%8F%AA%E9%80%82%E5%90%88%E5%8D%95%E6%9C%BA%E6%88%BF%E9%AB%98%E9%80%9F%E5%B1%80%E5%9F%9F%E7%BD%91%E9%83%A8%E7%BD%B2)
-   [限制: auto increment 默认是7, 集群建立起来之后不能改](%7B%7Bpage.url%7D%7D#%E9%99%90%E5%88%B6-auto-increment-%E9%BB%98%E8%AE%A4%E6%98%AF7-%E9%9B%86%E7%BE%A4%E5%BB%BA%E7%AB%8B%E8%B5%B7%E6%9D%A5%E4%B9%8B%E5%90%8E%E4%B8%8D%E8%83%BD%E6%94%B9)
-   [限制: 默认要设置为read-only](%7B%7Bpage.url%7D%7D#%E9%99%90%E5%88%B6-%E9%BB%98%E8%AE%A4%E8%A6%81%E8%AE%BE%E7%BD%AE%E4%B8%BAread-only)
-   [限制: 失联的节点不会自动加回到group里.](%7B%7Bpage.url%7D%7D#%E9%99%90%E5%88%B6-%E5%A4%B1%E8%81%94%E7%9A%84%E8%8A%82%E7%82%B9%E4%B8%8D%E4%BC%9A%E8%87%AA%E5%8A%A8%E5%8A%A0%E5%9B%9E%E5%88%B0group%E9%87%8C)
    -   [这里会有个问题: 失联节点还可以提供读操作](%7B%7Bpage.url%7D%7D#%E8%BF%99%E9%87%8C%E4%BC%9A%E6%9C%89%E4%B8%AA%E9%97%AE%E9%A2%98-%E5%A4%B1%E8%81%94%E8%8A%82%E7%82%B9%E8%BF%98%E5%8F%AF%E4%BB%A5%E6%8F%90%E4%BE%9B%E8%AF%BB%E6%93%8D%E4%BD%9C)

-   [限制: 2个成员里kill 1个member不能被自动处理, 因为2 成员中1个member不能独立行程多数派,整个group会卡主,不接受任何写入](%7B%7Bpage.url%7D%7D#%E9%99%90%E5%88%B6-2%E4%B8%AA%E6%88%90%E5%91%98%E9%87%8Ckill-1%E4%B8%AAmember%E4%B8%8D%E8%83%BD%E8%A2%AB%E8%87%AA%E5%8A%A8%E5%A4%84%E7%90%86-%E5%9B%A0%E4%B8%BA2-%E6%88%90%E5%91%98%E4%B8%AD1%E4%B8%AAmember%E4%B8%8D%E8%83%BD%E7%8B%AC%E7%AB%8B%E8%A1%8C%E7%A8%8B%E5%A4%9A%E6%95%B0%E6%B4%BE%E6%95%B4%E4%B8%AAgroup%E4%BC%9A%E5%8D%A1%E4%B8%BB%E4%B8%8D%E6%8E%A5%E5%8F%97%E4%BB%BB%E4%BD%95%E5%86%99%E5%85%A5)
-   [限制: 配置: 必须使用hostname](%7B%7Bpage.url%7D%7D#%E9%99%90%E5%88%B6-%E9%85%8D%E7%BD%AE-%E5%BF%85%E9%A1%BB%E4%BD%BF%E7%94%A8hostname)
-   [操作: my.cnf 中关于group replication的配置](%7B%7Bpage.url%7D%7D#%E6%93%8D%E4%BD%9C-mycnf-%E4%B8%AD%E5%85%B3%E4%BA%8Egroup-replication%E7%9A%84%E9%85%8D%E7%BD%AE)
-   [操作: 初始化mysql user 或 password时必须禁止binlog, 否则互相复制时会出现binlog冲突](%7B%7Bpage.url%7D%7D#%E6%93%8D%E4%BD%9C-%E5%88%9D%E5%A7%8B%E5%8C%96mysql-user-%E6%88%96-password%E6%97%B6%E5%BF%85%E9%A1%BB%E7%A6%81%E6%AD%A2binlog-%E5%90%A6%E5%88%99%E4%BA%92%E7%9B%B8%E5%A4%8D%E5%88%B6%E6%97%B6%E4%BC%9A%E5%87%BA%E7%8E%B0binlog%E5%86%B2%E7%AA%81)
-   [操作: 部署mysql group replication:](%7B%7Bpage.url%7D%7D#%E6%93%8D%E4%BD%9C-%E9%83%A8%E7%BD%B2mysql-group-replication)
-   [操作: 对group成员的管理](%7B%7Bpage.url%7D%7D#%E6%93%8D%E4%BD%9C-%E5%AF%B9group%E6%88%90%E5%91%98%E7%9A%84%E7%AE%A1%E7%90%86)
-   [操作: trouble shooting: 都挂了之后的启动](%7B%7Bpage.url%7D%7D#%E6%93%8D%E4%BD%9C-trouble-shooting-%E9%83%BD%E6%8C%82%E4%BA%86%E4%B9%8B%E5%90%8E%E7%9A%84%E5%90%AF%E5%8A%A8)
-   [参考:](%7B%7Bpage.url%7D%7D#%E5%8F%82%E8%80%83)

<!-- mdtoc end   -->

Mysql group replication 提供了比binlog replication更强的一致性集群解决方案.
最近在项目中尝试了1下, 有好处也有小坑, 记录1下.

<a class="md-anchor" name="依赖-group-replication-需要gtid支持多主复制基于gtid格式的binlog"></a>

## 依赖: group-replication 需要gtid支持,多主复制基于gtid格式的binlog

> In Group Replication, state transfers are fully based on binary logs with GTID
> positions.


<a class="md-anchor" name="特性-多主模式"></a>

## 特性: 多主模式:

mysql group replicaiton 支持两种模式: 单主和多主, 区别在于是否只允许primary
支持写入, 还是每个成员都可以写入.

-   不支持并发多个库上建立db/table:

    都可以创建成功, 然后error.log里报binlog apply冲突, 导致group复制全部终止.不知道怎么恢复.

-   支持并发多个库上插入数据:

    并发向多个member上写, 只有1个实例成功,在写入阶段就可以检测出冲突, binlog正常复制.

<a class="md-anchor" name="限制-group-replication-只适合单机房高速局域网部署"></a>

## 限制: group-replication 只适合单机房高速局域网部署

> The MySQL Group Replication documentation isn’t very optimistic on WAN
> support, claiming that both “Low latency, high bandwidth network connections
> are a requirement” and “Group Replication is designed to be deployed in a
> cluster environment where server instances are very close to each other, and
> is impacted by both network latency as well as network bandwidth.”


<a class="md-anchor" name="限制-auto-increment-默认是7-集群建立起来之后不能改"></a>

## 限制: auto increment 默认是7, 集群建立起来之后不能改

http://mysqlhighavailability.com/mysql-group-replication-auto-increment-configuration-handling/

<a class="md-anchor" name="限制-默认要设置为read-only"></a>

## 限制: 默认要设置为read-only

配置文件my.cnf里加配置:

> super-read-only = 'on'; # 防止刚刚启动的实例误写入没在group里的mysql.


在mysql group建立起来之后, 会自动清除这个标记.

<a class="md-anchor" name="限制-失联的节点不会自动加回到group里"></a>

## 限制: 失联的节点不会自动加回到group里.

在测试过程中, 一个节点失联后, primary会把它从组成员列表中去除. 必须手动加入.

> Separated nodes that lose the quorum will be expelled from the cluster, and
> won’t join back automatically once the network connection is restored. In its
> error log we can see:


需要手动加回:

```sh
mysql> START GROUP_REPLICATION;
ERROR 3093 (HY000): The START GROUP_REPLICATION command failed since the group is already running.
mysql> STOP GROUP_REPLICATION;
Query OK, 0 rows affected (5.00 sec)
mysql> START GROUP_REPLICATION;
Query OK, 0 rows affected (1.96 sec)
mysql> SELECT * FROM performance_schema.replication_group_members;
+---------------------------+--------------------------------------+--------------+-------------+--------------+
| CHANNEL_NAME | MEMBER_ID | MEMBER_HOST | MEMBER_PORT | MEMBER_STATE |
+---------------------------+--------------------------------------+--------------+-------------+--------------+
| group_replication_applier | 24d6ef6f-dc3f-11e6-abfa-0242ac130004 | cd81c1dadb18 | 3306 | ONLINE |
| group_replication_applier | 329333cd-d6d9-11e6-bdd2-0242ac130002 | f18ff539956d | 3306 | ONLINE |
| group_replication_applier | ae148d90-d6da-11e6-897e-0242ac130003 | 0af7a73f4d6b | 3306 | ONLINE |
+---------------------------+--------------------------------------+--------------+-------------+--------------+
3 rows in set (0.00 sec
```

<a class="md-anchor" name="这里会有个问题-失联节点还可以提供读操作"></a>

### 这里会有个问题: 失联节点还可以提供读操作

> Moreover, in Group Replication a partitioned node keeps serving dirty reads as
> if nothing happened.


<a class="md-anchor" name="限制-2个成员里kill-1个member不能被自动处理-因为2-成员中1个member不能独立行程多数派整个group会卡主不接受任何写入"></a>

## 限制: 2个成员里kill 1个member不能被自动处理, 因为2 成员中1个member不能独立行程多数派,整个group会卡主,不接受任何写入

遇到mysql不能自动调整membership的情况,需要人为介入, 通过

SET GLOBAL group_replication_force_members="127.0.0.1:10000,127.0.0.1:10001";

强制把集群修改为摸个设置.来解决group内不能形成多数派的情况.

force_member之后,
其他的member启动后可以自动加入(如果启动的member上没有group中不包含的事务的话)

<a class="md-anchor" name="限制-配置-必须使用hostname"></a>

## 限制: 配置: 必须使用hostname

在my.cnf 中,必须加入 一个配置: report-host, 让mysql使用这个值作为能找到它的hostname, group-replication只使用hostname来找组成员.

如果不指定这个值, 默认的hostname如localhost会被使用,导致group成员互相找不到彼此.

把这个值设置成ip就可以了

```dosini
[mysqld]

# let master use this address instead of
# default hostname, which might not be
# resolvable by master
report-host = your_ip
```

<a class="md-anchor" name="操作-mycnf-中关于group-replication的配置"></a>

## 操作: my.cnf 中关于group replication的配置

```dosini
#  Configuring group_replication_start_on_boot instructs the plugin to not start
#  operations automatically when the server starts. This is important when setting
#  up Group Replication as it ensures you can configure the server before manually
#  starting the plugin. Once the member is configured you can set
#  group_replication_start_on_boot to on so that Group Replication starts
#  automatically upon server boot.

# It shoudl be off when setting up a group.
# After that it should be `on` to let
# mysql auto starts group replicaton
# when restarted.


loose-group_replication_start_on_boot =  "on"

loose-group_replication_local_address = "my_ip:0123"
loose-group_replication_group_seeds = "my_ip:0123,other_ip:0123"

# "on" for one server deploy only.
loose-group_replication_bootstrap_group = off

# group replication requires this
# if using multi worker to apply binlog
slave-preserve-commit-order = 1

# use multi primary mode
loose-group-replication-single-primary-mode = 0

# to prevent write on non-group-member
super-read-only = "on"
```

<a class="md-anchor" name="操作-初始化mysql-user-或-password时必须禁止binlog-否则互相复制时会出现binlog冲突"></a>

## 操作: 初始化mysql user 或 password时必须禁止binlog, 否则互相复制时会出现binlog冲突

```sql
SET SQL_LOG_BIN=0;
SET PASSWORD FOR "root"@"localhost" = "password";
FLUSH PRIVILEGES;
SET SQL_LOG_BIN=1;'
```

<a class="md-anchor" name="操作-部署mysql-group-replication"></a>

## 操作: 部署mysql group replication:

配置binlog复制的channel(所有实例)

```sh
mysql -e 'CHANGE MASTER TO
    MASTER_USER="replicator"
  , MASTER_PASSWORD="replicator_password"
FOR CHANNEL "group_replication_recovery"'
```

检查group replication插件是否已经安装,没有则安装(只需执行一次)(所有实例)

```sh
mysql -e 'SELECT "ok" FROM mysql.plugin WHERE name = "group_replication"' \
    | grep ok \
    || mysql -e 'INSTALL PLUGIN group_replication SONAME "group_replication.so"'
```

检查是否bootstrap过了(在一个实例上)

```sh
mysql -e 'SELECT "booted" FROM performance_schema.replication_group_members WHERE MEMBER_ID != "";' \
    | grep booted

# bootstrap group replication, 如果没有启动过的话(在一个实例上)
mysql -e 'SET GLOBAL group_replication_bootstrap_group=ON;
    START GROUP_REPLICATION;
    SET GLOBAL group_replication_bootstrap_group=OFF;'
```

检查group replicaiton 状态

```sh
mysql -e 'SELECT "started" FROM performance_schema.replication_connection_status WHERE SERVICE_STATE = "ON";' \
    | grep started
```

其他成员加入(第一个实例之外)

```sh
mysql -e 'START GROUP_REPLICATION;'
```

<a class="md-anchor" name="操作-对group成员的管理"></a>

## 操作: 对group成员的管理

-   通过配置来指定要加入的group的节点都有哪些, 原则上每个成员都使用相同的组配置:

    ```dosini
    loose-group_replication_group_seeds           = "172.18.5.50:24999,172.18.5.135:24999,172.18.5.55:24999"
    ```

    这些节点只要有1个能够联系到就能正确加入到group中.

    加入之后的group membership(运行时的)可能和这个列表不同. mysql会动态调整

    这个配置只影响`start group_replication`时去哪找集群去加入.

-   mysql会动态的调整group membership,如:

    -   发现一个member联系不到;
    -   member被正常kill掉;
    -   网络中断等...

    能被处理的membership变化, mysql会自动调整, error.log里会看到以下信息:

    ```
    Plugin group_replication reported: 'Group membership changed to 172.18.5.55:3306 on view 15168862705781240:4.'
    ```

譬如 3个成员的group里1个member被kill掉.

用

```sql
SELECT * FROM performance_schema.global_status WHERE VARIABLE_NAME= 'group_replication_primary_member';
```

可以看到group从3个成员变成2个.

<a class="md-anchor" name="操作-trouble-shooting-都挂了之后的启动"></a>

## 操作: trouble shooting: 都挂了之后的启动

group-replication-force-members 在所有机器都挂了重启时用不了.

报错是:

`[ERROR] Plugin group_replication reported: 'group_replication_force_members must be empty on group start. Current value: '172.18.5.55:24999''`

第1个机器起来时,无法加入到一个现有的group, 拿不到group members列表. group_replication不能正常启动.

这时, group-replication-force-members 也无法设置.

---

多数派都挂了后, 需要重新走1下bootstrap 流程:

```sql
SET GLOBAL group_replication_bootstrap_group=ON;
START GROUP_REPLICATION;
SET GLOBAL group_replication_bootstrap_group=OFF;
```

<a class="md-anchor" name="参考"></a>

## 参考:

[battle-for-synchronous-replication-in-mysql-galera-vs-group-replication](https://www.percona.com/blog/2017/02/24/battle-for-synchronous-replication-in-mysql-galera-vs-group-replication/)

[Features_Pros_Cons_MySQL_Group_Replication.pdf](/post/mysql-group-replication/DV_WP-Features_Pros_Cons_MySQL_Group_Replication.pdf)



Reference:

