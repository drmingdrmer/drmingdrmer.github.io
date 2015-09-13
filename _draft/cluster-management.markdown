---
layout: post
title:  "可靠集群成员管理: 2 阶段paxos"
date:   
categories: tech distributed
tags: paxos distributed consensus consistency Raft cluster management membership
---

# 背景

大家知道分布式系统中的核心问题是让多个进程对某事达成一致,
这各种replication算法的核心问题，而replication是存储可靠的核心。
解决了这个问题才能在多机环境中建立可靠运行的分布式系统

关于达成一致这个问题，已经有了完备的解决方案，就是paxos。
大家可以参考我上一次的slides，对paxos算法建立一个直观的认识。

[可靠分布式系统基础-paxos的直观解释][paxos-slides]

## paxos 解决的问题和没有解决的问题

paxos定义了1个通用的一致性算法，让多个进程对一件事情达成一致。
这个算法在[paxos-made-simple][paxos-made-simple]论文中进行了完整的讨论。

在论文中的一个基本假设就是：

在运行paxos算法时，首先要知道参与这个算法的进程都有哪些，
也就是，集群的成员（进程）都有哪些。

如果在paxos运行过程中每个成员所知道成员列表不一致,
可以很容易构造出一个出错的例子，在这个例子中成员的不同的子集会对一件事情得出不同的结论。

因此，集群信息的一致性，是paxos正确运行，今儿对其他事情达成一致的前提。

但集群信息的一致性保证并没有在paxos算法本身中讨论。

在现实中，'集群中有哪些成员'这个问题是无法避免要去解决的。

因为无论多可靠的系统都会在长期运行中遇到一个问题，就是其中一个成员坏掉（或永久性下线）的问题。
要建立长期可靠运行的系统必须面对和解决成员替换的问题。

## 集群变更问题的简单解决方案

现实中有很多Tradeoff可以解决集群本身信息一致性的问题。

比如

-   集群信息静态保存，但及时替换损坏的成员并复制配置，让系统看起来没有成员变更过。

-   或限制每次成员变更的程度（如一次只增加或减少一个成员，并对paxos的quorum的稍加变化[link][link]）；


然而某些情况下（比如[sinastorage.com][sinastorage.com]），使用了几十万个paxos组来实现底层存储的自我调度和修复策略。
在这个场景中，必须有一个严密的成员信息管理的算法，来实现大规模的成员信息变更的自动化和程序化。


本文针对集群配置变更的问题，给出一个数学上可证明正确的通用算法，为paxos集群提供集群本身的信息的一致性保证。

(实际上就是在开发[sinastorage.com][sinastorage.com]时为了解决它而设计了这个算法)

# Cluster Config Management

实际运行的分布式集群中，一个集群要对一件事相互要达成一致之前，除了要达成一致的事情本身,
必须面临的是, 和谁达成一致的问题。

这就是集群配置管理的问题。

集群管理比leader election(或其他达成一致的问题)更基础。
先要解决集群里有谁的问题，才能解决和谁达成一致的问题。

leader election必须以集群信息为基础，
如果集群信息错误，leader election也运行不下去。

Raft的论文里讨论了一个简单的集群变更方案:

## Raft的集群配置变更算法

集群成员变更需要解决2个问题：

-   1个是必须让2组集群在时间上不能同时存在，在时间上必须有个barrier,
    避免新旧2个集群在同一时间都能选出leader。

-   第2个是，在任何1种进程死掉的场景中，都必须能让系统在有限时间内恢复回来。
    继续选出leader然后继续工作。

对第1个问题，
Raft使用一个中间状态去避免新旧2个集群都可以选出leader的问题。
(但没有解决都选不出leader的问题)

假设变更前后的集群配置分别为C-old 和 C-new。
C-old和C-new是两个不同的成员列表，系统需要从C-old变化到C-new并在整个过程中保证系统不能停机或不一致。

当系统处在这个中间状态的时候:

-   Raft使用的集群配置是C-old和C-new的成员并集: C-old-new

-   当系统处于中间状态时， 一个组成员成为多数派的条件是: 

    这组成员同时包含C-old的多数派，也包含C-new的1个多数派。

    也就是说，
    Quorum-old-new 和C-old 的交集是C-old的一个多数派，
    Quorum-old-new 和C-new 的交集是C-new的一个多数派，

-   当系统处于中间状态时，
    达成的一致被称作 joint consensus,
    达成一致的条件是在Quorum-old-new承认某事。


由原始的多数派（quorum）的定义：
    一个集群中的任意2个多数派交集必须不是空。

所以
这样: C-old的多数派和C-old-new的多数派互斥，C-old-new的多数派和C-new的多数派互斥。

在时间上, Raft变更集群的时候:
先把集群从C-old
变成C-old-new，标志是C-old-new中的多数派都认为集群是C-old-new。
这时C-old可能还有部分成员认为集群是C-old，但因为不够多数派,
就可以保证C-old不会再选出leader了。

然后raft再将系统配置更新到C-new。
同样当C-new中多数派认为系统配置是C-new时，C-old-new也将不再能选出多数派。

所以在整个变化过程中C-old和C-new在时间上被C-old-new隔离开不会同时选出leader。

保证中间任何一个时间最多只有1个leader。

最终集群信息变更为C-new。

通过以上步骤, Raft解决了变更过程中产生多主的问题。

但是这个算法并不能保证C-old和C-old-new都选不出主的情况...

## Raft的缺陷

**

但是这个算法并不能保证C-old和C-old-new都选不出主的情况。

譬如：
假设开始C-old = {a, b, c}
C-new = {c, d, e}

所以C-old-new = {{a, b, c}, {c, d, e}}

Raft的论文上说：

>   Once a given server adds the new configuration entry to its log, it uses that
>   configuration for all future decisions (a server always uses the latest
>   configuration in its log, regardless of whether the entry is committed). This
>   means that the leader will use the rules of C-old-new to determine when the
>   log entry for C-old-new is committed.

意思是说，当1个成员接受到变更集群信息的日志后就开始使用它了,
而不是确认提交之后才使用。

开始时, a b c都认为自己的集群信息是C-old, 它们希望将集群配置变更为c d e, d 和
e现在还是空的：
```
a - {a, b, c}
b - {a, b, c}
c - {a, b, c}
d - {}
e - {}
```

然后收到1条变更到C-old-new = {{a, b, c}, {c, d, e}}的日志，开始复制到其他成员
然后写到中途，所有的成员都挂了，然后所有成员都将重启，重新选leader，继续运行。

假设在最乐观的情况下，所有成员之间最多只相差一条日志, 
也就是说某些成员是`{a, b, c}`, 某些成员认为集群是`{{a, b, c}, {c, d, e}}`。
这种情况下很容易构造出一种状态：在这个状态下没有一个成员可以选出leader。

*Raft将集群变更的操作退化成了多数派写(quorum-write)，
而quorum-write的问题在于，
quorum-write
需要没有leader的情况下能将集群信息推到1个最终一致的状态来解决不一致，才能最终解决这个问题。*

例如, 下面是1个最简单的失败的例子：
```
a - {a, b, c}
b - {{a, b, c}, {c, d, e}}
c - {{a, b, c}, {c, d, e}}
d - {a, b, c}
e - {a, b, c}
```
这时C-old里的:
-   a 没有收到最后1条更新集群信息的日志，它们认为集群还是a, b, c
-   b, c 成员中的集群信息都更新成了C-old-new.
-   d, e 没有收到最后1条更新集群信息的日志，它们认为集群还是a, b, c

这时每个成员选举的结果是这样：

-   a 不能选自己为主，因为abc里有2个已经是C-old-new了，
    它必须拒绝旧配置C-old的选举, 以达到隔离C-old和C-new的barrier的效果。

-   b c 也不能选各自为主，因为cde里只有c知道C-old-new，d e都会拒绝b和c的选举。

-   d e 和a类似，它们的选举请求会被b和c拒绝。

因此这个情况下所有成员都重启后，每个成员都无法选出leader。

而Raft的leader是所有操作的前提，没有leader，集群就卡在了这里。

其实解决这个问题也很简单，只要允许日志可以在没有leader的情况下也能互相同步。
让整个系统中每个成员（a d e）都知道这个集群信息C-old-new，
达到最终一致，就可以再次运行起来。

而实际上这就是paxos的核心，对等的一组成员达成一致。


问题在于，在没有leader的情况下，Raft不知道哪个数据时committed。


只要知道哪个日志是committed，就可以解决这个问题。

但raft在leader选出之前不知道哪些日志是committed。

raft在leader选出之后由leader去想slave同步日志。

这里看起来是一个简化，但由此产生了集群变更时需要在没有leader的情况下将系统配置同步到一致的状态。
zookeeper使用了这个方法，先同步日志再选leader？


更改：
leader接到1个变更集群的消息时，将它写入日志但不启用，直到committed才使用。
这时


任何时候，如果C-old的多数派承认了C-old-new，而C-old-new中还没有多数派承认C-old-new
则会造成整个集群无法选主。

为解决这个问题，关键在于是否能在没有leader的情况下，
将C-old-new的多数派写入C-old-new

因为Raft所有日志通过都是基于leader的，所以必然会有些情况下造成集群挂起。

解决这个问题需要给Raft加入无leader的日志同步机制，
同时也需要在没有leader的情况下知道应该同步哪些日志。

这些正是paxos解决的问题。

要在无leader的条件下知道哪些日志是可以同步的，
而此时集群信息又处在变化中，不能直接进行paxos，
所以需要引入committed的日志来标示哪些日志是accepted。

accepted，被多数派收到，但不使用
committed，另外一条日志来记录哪个日志是被accepted。



...




一次只更新变化（添加或删除，不包括替换），就可以避免这个问题。

```
a - {{a, b, c}, {a, b, c, d}}
b - {{a, b, c}, {a, b, c, d}}
c - {a, b, c}
d - {}
```


```
a = {a, b, c}
b = {a, b, c}
c = {a, b, c}

a = {a, b, c}
b = {x, y, z}
c = {x, y, z}
x = {x, y, z}
y = {x, y, z}
z = {x, y, z}

a = {a, b, c}
x = {x, y, z}
y = {x, y, z}
z = {x, y, z}

a = {a, b, c}
b = {b, y, z}
x = {b, y, z}
y = {b, y, z}
z = {b, y, z}

a = {a, b, c}
b = {b, y, z}
y = {b, y, z}
z = {b, y, z}

a = {a, b, c}
b = {b, y, z}
y = {b, y, z}, {x, y, z}
z = {b, y, z}, {x, y, z}

a = {a, b, c}
b = {b, y, z}
y =            {x, y, z}
z =            {x, y, z}
```


因为Raft里定义：
只要看到1条集群变更的日志，就使用这条日志的内容作为集群信息。


Raft对这部分的讨论基本没有，在实现上使用了：
每次只能变更一个成员的策略来回避这个问题。

Raft的问题在于，它的日志数据是paxos的，但集群信息的管理实际上退化到了quorum
rw: 
写入即可读。丢掉了accepted的概念。




paxos可以看做是quorum rw的加强版，通过2次quorum rw来达到一致。

paxos能够达成一致是因为写入的数据不1定是accepted（即，不会再被修改的）

Raft 需要leader来确认最后1条日志是否已经是committed状态。

我们需要的算法是1个在任何时候中断都能继续下去的算法。

# 基于2次paxos的成员变更算法

由于有这样的依赖关系：

业务数据读写(chubby/zookeeper)依赖leader（或multiple paxos）;
leader依赖系统成员信息(membership);



假设这样一个模型：

-   paxos用来维护集群信息。

    一次paxos确定的值是1个集群中成员的配置(config).

-   每次变更的配置对应一个新的版本(ver)，同时每个版本对应paxos的一个instance。

-   版本号ver单调递增。

-   任何2个集群配置C1和C2, 即使包含的成员列表完全一样，也不认为是同样地集群。

    因为不同版本的集群可能误以为某个成员在集群里而做出错误的决策。

    配置的相等条件是版本号ver相等。



集群变更需要2个步骤：

1.  初始状态C-old, 目标配置C-new, 中间状态C-old-new

    3个配置的多数派Q-old，Q-new 和 Q-old-new
    Q-old-new 和 Q-old有交集
    Q-old-new 和 Q-new有交集

    假设C-old的ver是10，那么C-old-new这个中间状态的版本是11，最后C-new的版本是12。
    整个过程只产生2个版本。

    如果有多个进城同时想要更新集群配置，最终只有1个可以成功，成功的最终版本也是12。

    paxos运行时有3组消息(参考[]):
    -   phase-1
    -   phase-2 当proposer收到多数派的phase-2 的正确返回的时候，
        它就可以确认paxos决议要确定的值已经被系统确认下来不会再更改了。
        但这时每个Acceptor都不知道决议的值有没有被确定下来，Acceptor只知道自己接受的值。
        因此要引入第3个请求

    -   commit propoer成功运行phase-2后，
        proposer 发送commit消息给所有的acceptor，告之某个值已经被确定下来了。

        这时Acceptor可以知道哪个值被整个集群确定了，认为是有效的了。

        req: paxos-instance-id, value-accepted, 
        Acceptor 的记录到磁盘
        resp: OK|reject

        phase-3? what is it defined as in paxos?

一个值有3个状态：

proposed 被某个集群(由ver标示)
    提出但没有确定下来，也就是运行paxos来确定这个决议的过程没有完成phase-2
    
    这时某些Acceptor可能接受了这个值，有些还不知道，但接受了这个值的Acceptor没有达到多数派。


accepted 被某个集群(由ver标识)
    paxos在这个集群上运行完了phase-2，多数派接受了这个值，但这时只有发起决议额proposer知道值被集群确定下来了

committed
是Acceptor对一个值的状态，说明Acceptor知道这个值是accepted了，对这个Acceptor来说，它就是committed。
一个ver的值被确定后，之前的ver的值就

1.  某1个proposer P，开始更新集群信息。

    P 读取本地的集群信息，如果是C-new, 同步，并退出。

    P 在集群C-old上运行第1次paxos将ver=11的集群配置 C-old-new在C-old内达成一致。

    这个步骤里P可能遇到3种情况：


    1.  如果它发现某个Acceptor保存了committed的C-old-new(ver=11)，则直接运行步骤 3。

        因为被记录为committed肯定是accepted，所以安全不会产生不一致。
        这个分支最主要的产生原因是从上次集群配置更细失败的中重运行遇到。

    1.  完整的运行成功paxos，
        使得C-old中的多数派接受了下个要更新成的配置是C-old-new。


1.  然后P 以quorum write的策略(quorum = Q-old-new),
    向C-old-new中的所有成员发送commit消息，

    通知C-old-new内的所有成员使用新的集群信息C-old-new。
    收到commit消息的成员开始使用C-old-new作为集群的配置。

    这一步完成的条件是: 收到commit消息的Acceptor达到了C-old-new的Q-old-new。
    当多数派都接受了新的集群信息C-old-new后，就可以在后面的C-old-new中对一个决议运行paxos并达成一致。

    这时可以保证，C-old中的任何成员都不能产生多数派来完成任何paxos决议，
    因为接受了C-old-new的commit消息的C-old成员会拒绝其他版本(ver)的集群的任何消息。

    -   这一步如果失败，新的proposer P2重新开始运行

1.  当C-old-new的多数派收到了C-old-new的committed消息之后,
    整个集群就运行在C-old-new上了。

    这时可能还有C-old或C-new中某些成员不知道C-old-new，但他们不会再构成多数派了。

1.  在C-old-new集群上运行第2个paxos实例，将C-new的配置在C-old-new中达到accepted。

1.  向C-old-new中所有成员发送commit消息，通知成员使用C-new。

1.  这时只要C-new的多数派接受了commit(C-new)的消息，
    新的集群C-new就可以正常工作了。

    这时可能C-old中的成员还在使用C-old-new的配置。
    但因为C-old-new的配置需要在新旧2个集群里都达到多数派，
    所以C-old-new将不能选举或对任何信息达成一致。

    这时新的集群C-new可能已经不知道C-old-new的存在了。
    C-old中的成员使用C-old-new的配置再发起paxos时，会在C-new的成员上发现更新的committed的配置C-new。
    这时它直接将最新的committed 直接同步到本地。

1.  一个成员如果发现它不在它本地的committed的集群配置里，
    就直接将它自己删除掉。


整个算法里，在中端后如果committed 集群配置造成新旧都不能构成多数派：
因为已经committed了，所以再运行paxos或直接提交committed可以最终将系统配置信息
达成一致。

如果没有到committed环节，则运行paxos，或者会使用中断前的已写入的值，或者重新选择新的值写入。

2个步骤的写入C-old -> C-old-new -> C-new 避免了任意2个集群同时可以选主。

无主运行paxos，保证任一环节中断都可以继续运行下去而不产生不一致。

有点类似于2次two-phase-commit，
