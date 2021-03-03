
对于一个tcp连接，在c语言里一般有2种方法可以将其关闭：

```c
close(sock_fd);
```

或者

```c
shutdown(sock_fd, ...);
```

<!--more-->

多数情况下这2个方法的效果没有区别，可以互换使用。除了：

-   close() 是针对file的操作
-   shutdown() 是针对socket的操作

nix系统里socket是1个文件，但文件不1定是1个socket;

所以在进入系统调用后和达到协议层前(发出FIN包这一段),
close()和shutdown()的行为会有1点差异。

到达协议层以后，close()和shutdown()没有区别。

## 举几个栗子示范下close()和shutdown()的差异

下面通过几个例子演示下close()和shutdown()在多线程并发时的行为差异,
我们假设场景是:

-   `sock_fd` 是一个blocking mode的socket。
-   thread-1 正在对`sock_fd`进行阻塞的recv()，还没有返回。
-   thread-2 直接对`sock_fd`调用close() 或 shutdown()。
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

-   (1) thread-2 调用close()立即成功返回，这时recv()还在使用`sock_fd`。

    这里因为有另外1个线程thread-1正在使用`sock_fd`，
    所以只是标记这个`sock_fd`为要关闭的。
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

-   (1) thread-1还在等待`sock_fd`, thread-2调用shutdown(),
    立即开始关闭socket的流程，发FIN 包等。

    然后, 内核中`tcp_shutdown`中会调用[sock_def_wakeup](http://lxr.free-electrons.com/source/net/core/sock.c#L2212)
    唤醒阻塞在recv()上的thread-1。

-   (2) 这时recv()阻塞的线程被唤醒等待并立即返回。
    返回码是0，表示socket已经关了。

> 可以看到，shutdown()和close()不同，
> 会立即关闭socket的连接，并唤醒等待的recv()。


#### 以上2个例子的代码

[close-or-shutdown-recv](/post-res/close-shutdown/snippet/recv.c)

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

-   (1) thread-1还在等待`sock_fd`, thread-2调用shutdown(),
    立即开始关闭socket的流程，发FIN 包等。

    然后, 内核中`tcp_shutdown`中会调用[sock_def_wakeup](http://lxr.free-electrons.com/source/net/core/sock.c#L2212)
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

<strike>
当时注意到这个问题是在做1个go的server，因为在go的实现中，
一个tcp的accept的底层实现里，对accept()的系统调用还是阻塞的。

当另1个goroutine想要退出整个进程的时候，需要通知accept的goroutine先退出。

最初我使用`func (*TCPListener) Close`来关闭监听的socket,
但发现TCPListener:Close实际调用了系统调用close(),
无法唤醒当前正在accept()的goroutine,
必须等到有下一个连接进来才能唤醒accept()，
进而退出整个进程。

所以后来改成使用shutdown()来关闭`sock_fd`，以达到唤醒accept()的goroutine的目的。

</strike>

---

##### 更新 2015 Aug 05 - go中不能唤醒的问题和重现方法

(开始写的时候没有记清楚重现步骤，感谢 [foxmailed](http://weibo.com/foxmailed) 提醒。)

上面的描述不准确，更新一下,
实际上是2个问题在1起引起的`TCPListener.Close`无法唤醒Accept的goroutine:

-   go里的socket本来应该都是nonblocking的。

    go内部accept的系统调用在没有连接时返回-1，
    然后进入事件的等待(`epoll_wait`等)。

    执行`TCPListener.Accept`的goroutine如果没有收到connect请求,
    就把自己挂起来, 等待网络事件到来.

-   `TCPListener.Close` 本身是有的唤醒机制的。

    但和系统调用shutdown()的唤醒不一样，
    shutdown是线程调度层面的，
    `TCPListener.Close`是网络事件层和goroutine层面。

    `TCPListener.Close`实际上是把`TCPListener.Accept`的goroutine唤醒。
    所以正常的阻塞的`TCPListener.Accept`的goroutine在`TCPListener.Close`调用时会被唤醒.

    如果监听的TCPListener内部的fd时blocking模式的,
    它在调用系统调用accept()时, accept()不会返回-1, 而是阻塞住, 这时线程被挂起(不是goroutine挂起了).
    要唤醒就需要先把它从系统调用中唤醒(例如用shutdown,TCPListener.Close 没有这个步骤)。

    所以`TCPListener.Close`的唤醒机制前提是nonblocking。
    一旦进入blocking模式并调用了accept, `TCPListener.Close`就没能力把它唤醒了.

-   但go里面有1个问题，就是它的dup()实现时，
    每次dup之后还会顺手把fd设置为blocking模式:

    `net/fd_unix.go`里的实现, 看注释里地描述:

    ```
    func (fd *netFD) dup() (f *os.File, err error) {
            ns, err := dupCloseOnExec(fd.sysfd)
            if err != nil {
                    syscall.ForkLock.RUnlock()
                    return nil, &OpError{"dup", fd.net, fd.laddr, err}
            }

            // We want blocking mode for the new fd, hence the double negative.
            // This also puts the old fd into blocking mode, meaning that
            // I/O will block the thread instead of letting us use the epoll server.
            // Everything will still work, just with more threads.
            if err = syscall.SetNonblock(ns, false); err != nil {
                    return nil, &OpError{"setnonblock", fd.net, fd.laddr, err}
            }

            return os.NewFile(uintptr(ns), fd.name()), nil
    }
    ```

    简单说就是dup的副作用是把fd变成阻塞的，
    但go开发者不是很屌这件事情，觉得阻塞就阻塞，无非多用几个线程而已。

    可是`TCPListener.Close`的唤醒机制是必须基于nonblocking的。。。。。

-   所以只要dup()被调用了1下，
    `TCPListener.Close`就无法唤醒等待的`TCPListener.Accept`了。

    哪些场合dup会被调用呢？最简单地就是从Listener里取1下File对象就好了：

    ```
    l.(*net.TCPListener).File()
    ```

    go里File方法实现：

    ```
    net/tcpsock_posix.go:
    func (l *TCPListener) File() (f *os.File, err error) { return l.fd.dup() }
    ```

`.File()`在我们的代码里用在进程重启过程中的监听fd的继承.

为了解决这个问题, 我们在代码里每次调用`.File()`后，都加上了1句修正：

```
syscall.SetNonblock( int(f.Fd()), true )
```

下面这段代码可以重现go中Close不唤醒的问题：

[close-does-not-wake-up-accept.go](/post-res/close-shutdown/snippet/close-does-not-wake-up-accept.go)

```
package main
import (
    "log"
    "net"
    "runtime"
    "time"
)
func main() {
    runtime.GOMAXPROCS(2)
    l, err := net.Listen("tcp", ":2000")
    if err != nil {
    	log.Fatal(err)
    }

    show_bug := true
    if show_bug {
    	// TCPListener.File() calls dup() that switches the fd to blocking
    	// mode
    	l.(*net.TCPListener).File()
    }

    go func() {
    	log.Println("listening... expect an 'closed **' error in 1 second")
    	_, e := l.Accept()
    	log.Println(e)
    }()
    time.Sleep(time.Second * 1)
    l.Close()
    time.Sleep(time.Second * 1)
}
```

更新 2015 Aug 05 结束

---

#### 最后非常地感谢2位小伙伴，在追踪和定位这个问题时一起磕代码:DDD

[林小风](http://weibo.com/breezewoods)

[马健将](http://weibo.com/stupid)

[foxmailed](http://weibo.com/foxmailed)



Reference:

- sock_def_wakeup : [http://lxr.free-electrons.com/source/net/core/sock.c#L2212](http://lxr.free-electrons.com/source/net/core/sock.c#L2212)

- 马健将 : [http://weibo.com/stupid](http://weibo.com/stupid)

- 林小风 : [http://weibo.com/breezewoods](http://weibo.com/breezewoods)

- foxmailed : [http://weibo.com/foxmailed](http://weibo.com/foxmailed)


[sock_def_wakeup]:  http://lxr.free-electrons.com/source/net/core/sock.c#L2212
[马健将]:  http://weibo.com/stupid
[林小风]:  http://weibo.com/breezewoods
[foxmailed]:  http://weibo.com/foxmailed