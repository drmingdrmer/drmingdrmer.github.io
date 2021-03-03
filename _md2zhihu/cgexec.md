
<!-- mdtoc start -->

-   [问题: cgexec 会忽略掉 `LD_PRELOAD`的环境变量](%7B%7Bpage.url%7D%7D#%E9%97%AE%E9%A2%98-cgexec-%E4%BC%9A%E5%BF%BD%E7%95%A5%E6%8E%89--ldpreload-%E7%9A%84%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)
-   [解决方案](%7B%7Bpage.url%7D%7D#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88)
-   [原因](%7B%7Bpage.url%7D%7D#%E5%8E%9F%E5%9B%A0)

<!-- mdtoc end   -->

<a class="md-anchor" name="问题-cgexec-会忽略掉--ldpreload-的环境变量"></a>

# 问题: cgexec 会忽略掉 
`LD_PRELOAD`
的环境变量

有时需要替换malloc库的时候,
我们会使用`LD_PRELOAD=/usr/lib64/libtcmalloc.so.4 my_prog`
方便地将运行的malloc库替换成tcmalloc.

但是如果使用cgroup来启动`my_prog`, 这个环境变量就无法生效了.

验证这个问题, 可以通过一个 `test_preload.sh` 的脚本:

```sh
echo env:
env | grep LD # 显示是否继承了LD_PRELOAD的环境变量.

echo lsof:
lsof -p $$ | grep tcmalloc # 显示是否当前进程加载了tcmalloc
```

运行:

```
LD_PRELOAD=/usr/lib64/libtcmalloc.so.4 ./test_preload.sh
> env:
> LD_PRELOAD=/usr/lib64/libtcmalloc.so.4
> lsof:
> test_prel 7588 root  mem    REG  253,0    301136 36021701 /usr/lib64/libtcmalloc.so.4.4.5
```

通过cgexec运行时, 没有输出:

```
LD_PRELOAD=/usr/lib64/libtcmalloc.so.4 cgexec ./test_preload.sh
> env:
> lsof:
```

说明环境变量没有继承过来. 也没有被加载.

<a class="md-anchor" name="解决方案"></a>

# 解决方案

使用cgexec时, 必须把环境变量的指定放到cgexec启动之后:

```
cgexec sh -c 'LD_PRELOAD=/usr/lib64/libtcmalloc.so.4 ./test_preload.sh'
> env:
> LD_PRELOAD=/usr/lib64/libtcmalloc.so.4
> lsof:
> test_prel 10059 root  mem    REG  253,0    301136 36021701 /usr/lib64/libtcmalloc.so.4.4.5
```

<a class="md-anchor" name="原因"></a>

# 原因

可执行文件如果设置了capability属性或setuid属性(表示某些只有root级别才有的权限, 网卡抓包等),
就不允许LD_PRELOAD=tcmalloc.so 的环境变量来加载额外的lib,
因为安全性考虑, **不允许任意的代码跑到root身份上运行**.

例子:

```
# ping是设置了网络相关的capability所以普通用户才能抓包.

getcap /bin/ping
> /bin/ping = cap_net_admin,cap_net_raw+p

# 用非root用户运行:
LD_PRELOAD=/usr/lib64/libtcmalloc.so.4 ping baidu.com

# 拿到pid 29841:
lsof -p 29841 | grep tcmalloc
# 啥也没有

# 用root用户运行同样的命令:
LD_PRELOAD=/usr/lib64/libtcmalloc.so.4 ping baidu.com

# 可以看到允许被加载tcmalloc
lsof -p 2256 | grep tcmalloc
> ping    2256 root  mem    REG  253,0    301136 36021701 /usr/lib64/libtcmalloc.so.4.4.5
```

同样不允许通过环境变量加载so的属性还有setuid;

> setuid属性:
>    文件被执行时将自己的用户修改为文件所有者的用户, 而不是调用者的.


以及cgexec

[How to use cgroup...](https://access.redhat.com/solutions/1445073) 文中写的:

> They are required to launch, then classify as the application makes use of
> `LD_LIBRARY_PATH` which is not available when running a binary with **setuid** (such
> as cgexec).


**总之有机会把任意代码提升权限的事情都不会让做**.

使用cgexec加`LD_PRELOAD`需要这么做:

```
# 没有cgexec时:
LD_PRELOAD=/usr/lib64/libtcmalloc.so.4 ./test_preload.sh "a b" "c"

# 使用cgexec时:
cgexec sh -c 'LD_PRELOAD=/usr/lib64/libtcmalloc.so.4 ./test_preload.sh "a b" "c"'
```



Reference:

