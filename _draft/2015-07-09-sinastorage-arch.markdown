---
layout: post
title:  "Architecture of SinaStorage.com"
date:   2015 Jul 09
categories: tech arch
tags: arch object-storage ch paxos erasure-code haystack cross-idc replication
---

SinaStorage.com is an object storage system similar to Amazon S3.
In 2009 we started this project.
From scratch we built it up step by step.

#   Development And Deployment

All of our development and deployment are [git](git) based.
For development git is a great collaboration tool and for deployment
versioning is one essential part.

In our system version of each deployment is just a formatted git commit:

```
<date>-<hash>
```

##  GIT Working Flow

There has been a lot of git working flow.
[git-workflow](git-workflow)

And maybe the most famous workflow is [gitflow](gitflow)

We have one stable branch "master".

-   Code must be fully unit-tested and  in production
    enviroment.

-   There are several long-term `feature` branches in which actual
    modification is made.

-   Each file belongs to only one feature branch and can only be modified
    in its branch.

-   Master does not accept direct modification to it.
    All commits on master must be a `merge` of `featrue` commit.

### Pros:

-   It is much easier to track history of a batch of relevant files.

    Normally files for one feature are all in one directory so that it is easy
    to review changes with `git log directory_path`.
    But sometimes these file might distribute in different directories amount
    the entire working tree.

    Keeping files in a single branch makes it easier reviewing history with
    just `git log feature-branch-name`.

-   File renaming through history is more clear.

-   History rebasing for one specific feature is possible.

    Sometimes one change involves dozens of commits in several different
    feature branches.
    Keeping relavent files in its own branch makes it easier to re-write
    commit history, or rebase.
    Think about when one feature added invovles backend service changes and web
    UI changes.
    And one week quick hacking leaves a serial of messy commit history.
    Before pushing there should be a final step of re-organizing history to
    squash typo-fix commit or re-write readable commit messages.

    At such a time one feature per branch helps a lot.
    Even one can write some script to automate such mundane works, like I did.

-   Easier to split a module out of main project.
    `git subtree split` can do this.
    But it leaves two history with the same changes.
    It would be better to start a module in a separate feature branch at the
    first place.

    Also `git subtree split` messes up less history when splitting a feature
    branch than when splitting the entire git repository.

### Cons:

-   Sometimes it is hard to decide what branch a file should be in.
    One should always take time to make a good name.

-   If one change involves many branches. It takes minutes to commit each
    branch separately.
    But I have a script to do it for me.
    [commit-to-branch](url)

    And another script to find what branch a file belongs to.
    []()

##  GitLab

We use [GitLab]() as our git repository server.
It supplies almost everything we need in daily work.

-   Easy to setup.

-   For Authentication GitLab support LDAP backend authentication server.
    As there is already a LDAP auth server in our company for all kinds of
    third party system.

-   Pull-Request based collaboration.

-   Complete restful API.

    Initiating a new server in our cluster includes a step of push RSA public
    key to git repository server so that servers are able fetch codes.

-   Fine grained privilege control.

-   There are diff tool, history viewer and comment support web UI. But we do
    not use them a lot.

##  Versioned Deployment



There is a single version for each deployment.

A `version` is just a formatted git commit:
```
YYmmddhh-commit_hash
```

On each server the update daemon fetch code, compile and install.

Each update is atomic:

-   It creates a new directory with name like obove for each update.

-   After installing all of it, a symbolic link is created that points to
    this versioned directory, thus it makes new update visible.

-   If update process is killed for some reason, the half updated versioned
    directory becomes a junk and is left there until cleanup script finds it
    and removes it.
    A update directory will never be used twice.

-   After update, update script is responsible to shut down services of old
    version and start service of new version.
    But this is also unreliable, since update script has chance to be killed
    during updating and leaves some services not restarted.

    That's why we have a crontab script periodically checks service version
    and restarts them if service version is older than installed version.

-   This requires each of the services in our system to be aware of its own
    version.

    For restful services there is a special url that serves as version query
    API.
    It responds service revision in headers:
    ```
    > curl localhost/?extra&op=rev -v
    ...
    X-S2-REV: 15030214-1234567
    ...
    >
    ```

-   Monotonic incremental revision.

    Update script periodically check if there is new version to install.
    -   If local installed version is newer, it does nothing.
    -   If local installed version is stale, it fetches codes and install new
        version.

    This avoids the mistake of setting an old version, which might rewind the
    entire cluster to years ago.

-   Monotonic revisioning leads to the problem with fall back.
    If code with glitches is deployed to cluster, a manual fall back is
    required.

    In this case, a revision with old code but with newer commit date will be
    created to overwrite the malfunctioning code.

##  Zookeeper

The information of what version to upgrade to is recorded in zookeeper
cluster.

We have a zookeeper cluster of 9 nodes across 3 IDC, 3 nodes in each IDC.

#   Roles And Services

In our cluster all of the servers are installed with the same code(except
during leveled deployment).

Roles are assigned to each server to ...

Services and scripts are binded to roles.
-   Service or script can belongs to more than one role.

Following is role/service mapping in our system:
```
```

#   Front Node

Role Front is the restful API layer in our system.
It talks to web browsers or other client application.

There are several essential services for role Front:
-   `nginx-front` the nginx
-   `task-scheduler`
-   `log-trans`
-   ...

Our Front service is built mainly on top of nginx and
[lua-nginx](lua-nginx) module.

##  Nonblocking Programming Model With Nginx And Lua

Since nginx is single threaded server, not to block the entire process is
important.

[lua-nginx](lua-nginx) supplies a rich set of synchronous but nonblocking
socket API that makes streaming processing very easy.

lua-nginx hides the detail of event processing like `epoll_wait`.

When `socket.receive()` is called, lua-nginx does all of the work for you:
-   Pause current lua coroutine.
-   Add the socket into epoll and wait for a "ready to read" event to come.
-   Resume current lua coroutine that waiting for the socket.

```lua
local sock, err = ngx.req.socket()
while true do
    -- receive() puts current coroutine to sleep and wake it up when data is
    -- ready.
    local buf, err = sock:receive(1024*1024)
    do_something_with(buf)
end
```

### Issues With Lua Nginx

When you trying to read data that is not ready, lua-nginx hangs up current
coroutine and starts dealing with other event(read or write), before your data
become ready.
Not to starve other events.

But there is still a chance that a coroutine would starve others:

When there is always data to read or write, a coroutine keeps working, without
giving other event a chance to be delt with.

This is actually not an issue with lua, but an issue with nginx.
Any nginx module dealing with a request should not run for a long time.
Most of the time, a nginx module gives control back to nginx when there is no
data to read/write.
But if there is always data to read/write, a nginx module should explicitly
hang itself up and give control to nginx and then nginx could schedule other
request.

And this applies to script written for lua-nginx module.
There are several starving causes:
-   There is a lot data to read and CPU is not quick enough.
    Then it just reads for ever.
    This is not likely to happen normally.

-   A coroutine pipes one file to another with a while-true-loop.
    -   After reading data from file A, it takes several milliseconds sending
        data to file B.
    -   And now if another chunk of data arrived on file A.
    -   This coroutine then starts a new round of read-then-write and never
        stops until all of the maybe 1GB file transfered from A to B.

    In this case, an explicit `yield` is necessary. Normal a simple sleep is
    enough:
    ```lua
    local sock_a, err = ngx.req.socket()
    local sock_b, err = ngx.socket.tcp()
    while true do
        local buf, err = sock_a:receive(1024*1024)
        local bytes, err = sock_b:send(buf)
        ngx.sleep(0.001) -- explicit yield
    end
    ```

-   And the case in which starving is most likely to happen is:
    when a coroutine pipe data between network socket and a fs file
    descriptor.

    Because a file descriptor to a local file does not support polling(like
    epoll):
    it is always ready to read or write. Thus reading/writing to fs file
    descriptor never hangs current coroutine.

    Like above, one should always yield coroutine after reading/writing a
    chunk of data or it starves other coroutine.
    ```lua
    local sock_a = ngx.req.socket()
    local fd = io.open("/tmp/x")
    while true do
        local buf, err = sock_a:receive(1024*1024)
        local bytes, err = fd:write(buf)
        ngx.sleep(0.001) -- explicit yield
    end
    ```


But now, please be aware of that, it is not other **coroutine** but other
**event**.
This implies that there is still a chance your coroutine would starve others:

When a coroutine deals with 2 file descriptor.

Because there is only a simple and naive io-scheduler inside nginx: the 

#   Cluster Management
##  Journal Based Node Management
### Global Registry
### Local Cache

#   Meta Data Sharding And Re-Sharding

##  Based On Mysql

#   Stats
##  To Manage What You Have
##  Memcached Cluster
### Consistent Hash
### Proxy

##  Time Based Space Allocation

Comparison to sha1-based allocation

Pros
Cons

#   Where To Write
##  Rank Of Hard Drives
##  Group
##  Consistency Between Replicas

On each partition there is a script that compares file list between itself and
other replicas.
If a missing file found on local partition, this script fetch the file from
replica.

This script runs every night.

##  Correctness Of File Content

Besides  the second part of file correctness maintainace 

##  Distributed Storage and Centered Management
### Move Data Out Of Dead Node

Besides missing file and corrupted file, another issue is the down time of a
server.

#### Multiple IDC Aliveness Watching

If a storage server is down, data should be rebuild on other partition on
other server.

In our system a server that can not serve requests is marked as being down.

And here is the problem:
there is not a easy way to determine if a server is down for ever, or
temporarily due to network problem or server maintainance.

If the server is down for ever, data must be rebuilt.
Otherwise, nothing should be done because data rebuild brings a lot useless IO
in the cluster.

Thus the key is to determine whether a server is going down.

We built a probing network to detect down server:

-   9 probes in 3 IDC. 3 probes in each IDC.
    Network between IDC is much worse then inside IDC.

-   Each probe send message to every server in our cluster every minute.
    And servers that does not repond are recorded locally on the probe server.

-   Every minute, a colletor query all the probes about liveness of every
    server.

-   If a quorum of probes report dead about a server, this server is marked as
    dead.

    Quorum means:

    -   2 or more than 2 IDC reported liveness. If collector receives only
        data from 1 IDC, Even if all of the 3 probes in this IDC report a server
        dead, it is possible that the network of this IDC is down.

    -   2 or more than 2 probes in a IDC reported liveness.
        Since a probe might report a server dead because of wrongly configured
        local route table.

-   A collector tracks liveness of all servers.

    if a server stays dead for more than 15 minutes, this collector marks the
    server "definitely down".

    Then data migration will be triggered to rebuild data from other replica.

    And the "definitely down" server will go back to cluster if it is
    rebooted or reinitialized.


### Move Data Out Of Low Space Drive

When a hard drive runs out of space( free space < 2% ), auto rebalance is
triggered to move some data to other free hard drive.

-   The problem is that space will not be freed before migration completes.
    during this time, free space watcher keeps

### Manually Data Moving

#   Hot Data and Warm Data

In Sinastorage, most data is warm data, which is read once an hour or
less.
But most recent uploaded data is hot, which is read once per second or more.

We separate hot data storage and warm data storage.

After about 3 months hot data becomes warm data.

After 3 months we compact each `group` into a `erasure code` group.

#   Storage Node
##  One Process Per Drive

Before years we use the 1 process for all drive pattern.

This is simple and easy to manage. But:

-   1 slow drive will eventually block all running threads.
    Thus no request can be served.

After a while we switched to 1 process per drive pattern.

-   Each drive has a unique id universially in cluster.

-   Each drive has a unique index in the host server.

-   There is a bidirection mapping between drive index and the port the drive
    serves on.

## Drive Process Life Cycle

-   At first drive is added by administrator, when a unique id and a unique
    index are generated.

    the unique id is written to hard drive as uuid. Also a directory named
    of the unique id is created on the drive, as the `root` of all kinds of
    data: files, corrupted files and migration sessions etc.

    And then the unique id is registered in cluster database.

-   
-   A drive is removed from cluster in two ways:
    -   Administrator manually removes it.

-   Once a drive is removed from cluster it can not be added back with the
    same unique id.

##  Membership Management

Warm data is stored in erasure code group.
Each group is about 20GB in size and contains 16 member.

In each group there are 12 data members, which serves file access request.

-   A member is a directory on a drive.

    Any 2 member in one group must not be on the same drive or the same
    server.
    This way the probability of more than one members down at the same time is
    reduced.

-   One nginx process serves for all members on its drive.

-   The member directory contains:
    -   






### Classic Paxos

### Two Phase Member Change Algorithm
#### Safety And Proof

##  Haystack Like Storage Engine
### On-disk Layout
### Layered Index
### Size of In-memory Index

##  Erasure Code In SinaStorage
### Vandermonde Matrix
### LRC: Local Reconstruction Codes
### 

##  Self Health Check And Recovery
### Recover Damaged
### Probability Of Data Loss

[git]: https://github.com/git/git
[git-workflow]: https://www.atlassian.com/git/tutorials/comparing-workflows/centralized-workflow
[gitflow]: http://nvie.com/posts/a-successful-git-branching-model/
[lua-nginx]: 
