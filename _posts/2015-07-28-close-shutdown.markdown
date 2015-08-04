---
layout: post
title:  "socket关闭:close()和shutdown()的差异"
date:   2015 Jul 28
categories: tech programming network
tags: socket network close shutdown c EINVAL
---

对于一个tcp连接，在c语言里一般有2种方法可以将其关闭：

```c
close(sock_fd);
```

或者

```c
shutdown(sock_fd, ...);
```

多数情况下这2个方法的效果没有区别，可以互换使用。除了：

-   close() 是针对file的操作
-   shutdown() 是针对socket的操作

nix系统里socket是1个文件，但文件不1定是1个socket;

所以在进入系统调用后和达到协议层前(发出FIN包这一段),
close()和shutdown()的行为会有1点差异。

<!--more-->

到达协议层以后，close()和shutdown()没有区别。

## 举几个栗子示范下close()和shutdown()的差异

下面通过几个例子演示下close()和shutdown()在多线程并发时的行为差异,
我们假设场景是:

-   sock_fd 是一个blocking mode的socket。
-   thread-1 正在对sock_fd进行阻塞的recv()，还没有返回。
-   thread-2 直接对sock_fd调用close() 或 shutdown()。
-   不考虑linger。

## 栗子1: socket阻塞在recv()上, 调用close()

```
// Close a waiting recv()
Time
 |
 |  thread-1                  | thread-2           | tcpdump
 |                            |                    |
 |  recv(sock_fd              |                    |
 |      <unfinished ...>      |                    |
1|                            | close(sock_fd) = 0 |
 |                            |                    | // Some data arrived
 |                            |                    | // after close()
2|                            |                    | < seq 1:36 ... length 35
 |                            |                    | > ack 36 ...
 |  // Data was received.     |                    |
3|  <... recv resumed>) = 35  |                    |
4|                            |                    | > FIN sent
 |                            |                    | < ack of FIN received
 |                            |                    | ...
 |  // Can't be used any more |                    |
5v  recv(sock_fd) = -1        |                    |
```

在上面的例子里：

-   (1) thread-2 调用close()立即成功返回，这时recv()还在使用sock_fd。

    这里因为有另外1个线程thread-1正在使用sock_fd，
    所以只是标记这个sock_fd为要关闭的。
    socket并没有真正关闭。

    这时recv()还继续处于阻塞读取状态。

-   (2) close()之后，有些数据到了，recv可以读取并返回了。

-   (3) recv()收到数据, 正确退出。

-   (4) rece()结束调用，释放socket的引用，这时底层开始关闭socket的流程。

-   (5) 再次调用recv()就会得到错误。

> 可以看到，close()没有立即关闭socket的连接，也没有打断等待的recv()。

## 栗子2: socket阻塞在recv()上, 调用shutdown()

```
// Shutdown a waiting recv()
Time
 |
 |  thread-1                  | thread-2              | tcpdump
 |                            |                       |
 |  recv(sock_fd              |                       |
 |      <unfinished ...>      |                       |
1|                            | shutdown(sock_fd) = 0 | > FIN sent
 |                            |                       | < ack of FIN received
 |                            |                       | ...
 |  // Woken up by shutdown() |                       |
 |  // no errno set           |                       |
2|  <... recv resumed>) = 0   |                       |
 v                            |                       |
```

在上面的例子里：

-   (1) thread-1还在等待sock_fd, thread-2调用shutdown(),
    立即开始关闭socket的流程，发FIN 包等。

    然后, 内核中tcp_shutdown中会调用[sock_def_wakeup]
    唤醒阻塞在recv()上的thread-1。

-   (2) 这时recv()阻塞的线程被唤醒等待并立即返回。
    返回码是0，表示socket已经关了。

> 可以看到，shutdown()和close()不同，
> 会立即关闭socket的连接，并唤醒等待的recv()。

#### 以上2个例子的代码

[close-or-shutdown-recv](/snippet/close-shutdown/recv.c)


## 栗子3: socket阻塞在accept()上, 调用shutdown()

类似的，对阻塞在accept()上的socket调用shutdown()，accept也会被唤醒:

```
// Shutdown a waiting accept()
Time
 |
 |  thread-1                      | thread-2
 |                                |
 |  accept(sock_fd                |
 |      <unfinished ...>          |
1|                                | shutdown(sock_fd) = 0
 |                                |
 |  // Woken up by shutdown()     |
 |  // errno set to EINVA         |
2|  <... accept resumed>) = -1    |
 |                                |
 v                                |
```

-   (1) thread-1还在等待sock_fd, thread-2调用shutdown(),
    立即开始关闭socket的流程，发FIN 包等。

    然后, 内核中tcp_shutdown中会调用[sock_def_wakeup]
    唤醒阻塞在accept()上的thread-1。

-   (2) 这时在accept()上阻塞的线程被唤醒, 并立即返回。

    返回码是-1，errno设置为EINVA。

-   这里如果thread-2调用的是close(),
    accept不会被唤醒，如果后面有请求connect进来，还能正确接受并返回。

## 结论

-   shutdown() 立即关闭socket;

    并可以用来唤醒等待线程;

-   close() 不一定立即关闭socket(如果有人引用, 要等到引用解除);

    不会唤醒等待线程。

现在大部分网络应用都使用nonblocking socket和事件模型如epoll的时候，
因为nonblocking所以没有线程阻塞,
上面提到的行为差别不会体现出来 。

当时注意到这个问题是在做1个go的server，因为在go的实现中，
一个tcp的accept的底层实现里，对accept()的系统调用还是阻塞的。

当另1个goroutine想要退出整个进程的时候，需要通知accept的goroutine先退出。

最初我使用`func (*TCPConn) Close`来关闭监听的socket,
但发现TCPConn:Close实际调用了系统调用close(),
无法唤醒当前正在accept()的goroutine,
必须等到有下一个连接进来才能唤醒accept()，
进而退出整个进程。

所以后来改成使用shutdown()来关闭sock_fd，以达到唤醒accept()的goroutine的目的。

#### 最后非常地感谢2位小伙伴，在追踪和定位这个问题时一起磕代码:DDD

[林小风][林小风]
[马健将][马健将]

[sock_def_wakeup]: http://lxr.free-electrons.com/source/net/core/sock.c#L2212
[马健将]: http://weibo.com/stupid
[林小风]: http://weibo.com/breezewoods
