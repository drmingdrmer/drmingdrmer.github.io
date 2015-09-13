---
layout: post
title:  "用 Paxos 建立可靠系统"
date:   
categories: tech distributed
tags: paxos distributed consensus consistency raft
---

本文讨论分布式系统中的可靠性, 可靠性的基础是存储的可靠性，
db，object或块存储等，
最终取决于能否有效地在不可靠的介质(磁盘)上，建立相对可靠地存储。

多副本成为最直接的思路。

而多副本中的最主要问题就是如何维持各个副本之间的一致性。

本文希望带给读者一个对paxos的感性认识，不包含数学证明。

本文首先分析几个不同的复制模型的问题，

并讨论他们的可靠性和一致性，
排除不可靠方案，得出quorum rw的算法。

在quorum rw的基础上，提出原子性写入的要求，从而推导得出paxos的算法。


