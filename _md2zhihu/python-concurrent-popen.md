
<!-- mdtoc start -->

-   [表现](%7B%7Bpage.url%7D%7D#%E8%A1%A8%E7%8E%B0)
    -   [重现问题的代码](%7B%7Bpage.url%7D%7D#%E9%87%8D%E7%8E%B0%E9%97%AE%E9%A2%98%E7%9A%84%E4%BB%A3%E7%A0%81)

-   [解决方法](%7B%7Bpage.url%7D%7D#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
-   [原因](%7B%7Bpage.url%7D%7D#%E5%8E%9F%E5%9B%A0)

<!-- mdtoc end   -->

<a class="md-anchor" name="表现"></a>

# 表现

<!--excerpt-->

一个父进程里多个线程并发地调用`subprocess.Popen`来创建子进程的时候,
会有几率出现`Popen`长时间不返回的情况.

这个问题是由于fd被多个子进程同时继承导致的.

**感谢评论中的 周波 的提醒:**

> python3.4 CentOS Linux release 7.3.1611 (Core), 默认值已经是True


**这个问题只作为一个case来分享, 高版本的python不必再担心啦~**

<a class="md-anchor" name="重现问题的代码"></a>

## 重现问题的代码

下面这个小程序启动2个线程, 每个线程各自(通过`subprocess.Popen`)启动一个子进程,
一个子进程执行`echo 1`后就直接返回;
另一个子进程启动后, `sleep 0.03`秒后返回.

程序里统计了2个调用`Popen`花的时间,
运行后可以发现, echo的进程有时启动很快(小于预期的0.01秒, 仅仅是启动, 不包括执行时间),
有时会很慢(超过0.03秒), 刚好和另一个sleep的进程执行时间吻合.
调大sleep子进程的时间可以看到echo也会同样有几率返回慢.

<!--more-->

```python
# > cat slow.py
import threading
import subprocess
import time

def _open(cmd, expect):

    t0 = time.time()
    proc = subprocess.Popen(
            cmd,
            shell=True,
            # # without this line, some Popen does not return at once as expected
            # close_fds=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE)

    spent = time.time() - t0
    if spent > expect:
        print cmd + ' spent: ' + str(spent)

    proc.wait()


for ii in range(100):
    ths = [
            threading.Thread(target=_open, args=('echo 1', 0.01)),
            threading.Thread(target=_open, args=('sleep 0.03', 0.05)),
    ]

    for th in ths:
        th.start()

    for th in ths:
        th.join()

# > python2 slow.py
# echo 1 spent: 0.0381829738617
# echo 1 spent: 0.041118144989
# echo 1 spent: 0.0417079925537
# echo 1 spent: 0.0421600341797
# echo 1 spent: 0.039479970932
# ...
```

运行环境:

```sh
# uname -a
Linux ** 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux

# python2 --version
Python 2.7.5

# cat /etc/*-release
CentOS Linux release 7.2.1511 (Core)
```

<a class="md-anchor" name="解决方法"></a>

# 解决方法

`Popen`时加上`close_fds=True`, 保证fd不会被多个子进程继承.

```python
proc = subprocess.Popen(
        cmd,
        close_fds=True, # here
        ...
        )
```

<a class="md-anchor" name="原因"></a>

# 原因

直接原因是因为有并发时, Popen中创建的pipe没有被关闭,
导致父进程认为子进程还没启动成功而一直阻塞.

这里的`Popen`的过程, 包括:

-   父进程创建通信的管道(调用`os.pipe()`)
-   fork子进程
-   父进程通过pipe阻塞读取子进程的启动后的错误消息, 确认失败;
-   或读取到EOF(pipe在子进程exec时被关闭), 确认成功.

Popen 调用的最核心的代码是`subprocess.py` 中的 `_execute_child`,
问题的原因可以从下面这段简化版的代码中看到:

```python

def pipe_cloexec(self):
    # 1) 创建pipe用于父子进程通信...
    r, w = os.pipe()
    self._set_cloexec_flag(r)
    self._set_cloexec_flag(w)
    return r, w

def _execute_child(self, args, executable, preexec_fn, close_fds,
                   cwd, env, universal_newlines,
                   startupinfo, creationflags, shell, to_close,
                   p2cread, p2cwrite,
                   c2pread, c2pwrite,
                   errread, errwrite):
    # 1) 创建pipe用于父子进程通信...
    errpipe_read, errpipe_write = self.pipe_cloexec()
    try:
        try:
            # 2) 3)
            self.pid = os.fork()
            if self.pid == 0:
                # 子进程流程
                try:
                    # 5) 子进程关闭读的pipe: 不需要接受父进程的消息
                    os.close(errpipe_read)

                    # 如果需要, 子进程关闭所有打开的文件描述符.
                    # 只留下用于告之父进程错误的pipe
                    if close_fds:
                        self._close_fds(but=errpipe_write)

                    # 7) 子进程加载程序
                    os.execvp(executable, args)

                except:
                    exc_type, exc_value, tb = sys.exc_info()
                    exc_lines = traceback.format_exception(exc_type,
                                                           exc_value,
                                                           tb)
                    exc_value.child_traceback = ''.join(exc_lines)

                    # 通过pipe通知父进程错误信息
                    os.write(errpipe_write, pickle.dumps(exc_value))

                # 子进程如果出错, 直接退出. 退出会关闭所有pipe
                os._exit(255)

            # 以下是父进程的流程
        finally:
            # 4) 父进程不需要通知子进程错误消息, 直接关闭pipe的写入端.
            os.close(errpipe_write)

        # 6) 父进程阻塞的读取子进程发来的错误消息.
        data = _eintr_retry_call(os.read, errpipe_read, 1048576)
    finally:
        # 无论成功与否, 父进程不再需要从子进程读取任何消息了, 关闭pipe的读取端.
        os.close(errpipe_read)

    if data != "":
        # 父进程的错误处理...
    # 8) 9)
```

我们把上面的代码的执行过程整理成时间表, 如下:

<table>
<tr class="header">
<th style="text-align: left;">步骤</th>
<th>时间</th>
<th>动作</th>
<th>echo线程</th>
<th>sleep线程</th>
<th style="text-align: right;">父进程打开的fd</th>
<th style="text-align: right;">echo子进程的fd</th>
<th style="text-align: right;">sleep子进程的fd</th>
</tr>
<tr class="odd">
<td style="text-align: left;">1</td>
<td>0.00</td>
<td>创建通信的pipe</td>
<td>4,5=os.pipe()</td>
<td>6,7=os.pipe()</td>
<td style="text-align: right;">4,5,6,7</td>
<td style="text-align: right;">-</td>
<td style="text-align: right;">-</td>
</tr>
<tr class="even">
<td style="text-align: left;">2</td>
<td>0.00</td>
<td>echo线程fork</td>
<td>fork</td>
<td>-</td>
<td style="text-align: right;">4,5,6,7</td>
<td style="text-align: right;">4,5,6,7</td>
<td style="text-align: right;">-</td>
</tr>
<tr class="odd">
<td style="text-align: left;">3</td>
<td>0.00</td>
<td>sleep线程fork</td>
<td>-</td>
<td>fork</td>
<td style="text-align: right;">4,5,6,7</td>
<td style="text-align: right;">4,5,6,7</td>
<td style="text-align: right;">4,5,6,7</td>
</tr>
<tr class="even">
<td style="text-align: left;">4</td>
<td>0.00</td>
<td>父进程关闭写pipe</td>
<td>close(5)</td>
<td>close(7)</td>
<td style="text-align: right;">4,-,6,-</td>
<td style="text-align: right;">4,5,6,7</td>
<td style="text-align: right;">4,5,6,7</td>
</tr>
<tr class="odd">
<td style="text-align: left;">5</td>
<td>0.00</td>
<td>子进程关闭读pipe</td>
<td>-</td>
<td>-</td>
<td style="text-align: right;">4,-,6,-</td>
<td style="text-align: right;">-,5,6,7</td>
<td style="text-align: right;">4,5,-,7</td>
</tr>
<tr class="even">
<td style="text-align: left;">6</td>
<td>0.00</td>
<td>父进程阻塞读</td>
<td>read(4)…</td>
<td>read(6)…</td>
<td style="text-align: right;">4,-,6,-</td>
<td style="text-align: right;">-,5,6,7</td>
<td style="text-align: right;">4,5,-,7</td>
</tr>
<tr class="odd">
<td style="text-align: left;">7</td>
<td>0.00</td>
<td>子进程exec, 关闭自己的的pipe-fd</td>
<td>-</td>
<td>-</td>
<td style="text-align: right;">4,-,6,-</td>
<td style="text-align: right;">-,-,6,7</td>
<td style="text-align: right;">4,5,-,-</td>
</tr>
<tr class="even">
<td style="text-align: left;">8</td>
<td>0.01</td>
<td>echo子进程结束, sleep线程返回</td>
<td>-</td>
<td>read(6):done</td>
<td style="text-align: right;">4,-,6,-</td>
<td style="text-align: right;">-,-,-,-</td>
<td style="text-align: right;">4,5,-,-</td>
</tr>
<tr class="odd">
<td style="text-align: left;">9</td>
<td>0.03</td>
<td>sleep子进程结束, echo线程返回</td>
<td>read(4):done</td>
<td>-</td>
<td style="text-align: right;">4,-,6,-</td>
<td style="text-align: right;"></td>
<td style="text-align: right;">-,-,-,-</td>
</tr>
</table>

`Popen` 调用时创建1对pipe和子进程通信, `Popen`返回时,
子进程就已经创建成功, pipe也在子进程exec时关闭了.

但如果同时有2个`Popen`在调用, 父进程中会同时出现2对或几对pipe.

这几对pipe会在fork时被继承到子进程.
子进程在进行exec之前(创建pipe时), 已经将pipe的fd设置FD_CLOEXEC:
执行exec时自动关闭fd.
**但可能其他线程的pipe-fd还没有对其进行这个设置**(步骤1中`pipe_cloexec`的`os.pipe()`之后, 发生了fork).

因此, 如果并发地调用`Popen`, 1个子进程会在fork时带着为别的子进程准备的pipe fd,
并且不会关闭它们(因为子进程只知道自己的pipe fd, 没有设置`close_fds`时, 它不会鲁莽地关闭其他fd)!
这样1个pipe fd本应在父子进程这2个进程之间共享, 却意外地会在3个或更多的进程中处于打开状态.

而父进程中的Popen在阻塞的read pipe, 自己的子进程exec后自动关闭了这个pipe fd,
进而让父进程结束read, 但还有另外一个进程在打开着这个pipe fd(步骤7)(我们的例子中是sleep子进程继承了echo 子进程的pipe fd并且没有关闭),
父进程中的read不会检查到fd关闭, 一直保持阻塞读的状态.

直到所有继承了这个pipe fd的进程都退出了, 父进程的read才能结束(sleep子进程退出时,
自动关闭了所有fd, 包括为echo子进程准备的pipe fd,
到此时父进程read才能收到1个EOF并退出read的阻塞).



Reference:

