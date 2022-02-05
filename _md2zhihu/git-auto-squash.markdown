
使用git的同学是不是经常纠结于在开发过程中是应该频繁提交，
还是仔细构造提交点之后再提交？

-   前者可以让开发更流畅，不必打断思路，但会造成提交历史无法浏览；
-   后者可以构造漂亮易懂的提交历史，但码码时停下来考虑commit message
    怎么造句是不是太影响情绪了。

一般的做法是先做很多小的fixup，之后再将fixup合并到一起。

这个工具 `git-auto-squash` 可以将提交历史中连续的fixup
合并到它之前最早的1个正式提交点上，类似不需要交互的`rebase --interactive`。

<!--more-->

```sh
git-auto-squash
  Rewrite history to squash all commits wiht message starts with
  'fixup!' to its first parent. By drdr.xp@gmail.com

Usage:
  > git-auto-squash [-f] [-p <pattern>] <rev-list options>...

Options:
  -f            Force to remove backup ref from previous git-auto-squash.

  -p <pattern>  Squash commits with mssage starts with <pattern>.
                By default <pattern> is 'fixup!'.

  -t            Update all ref touched. Usefull when squashing history with
                merges.
                By default, with a repo like:
                    * a6910e2 (master) Merge commit '75275ed'
                    |\
                    | * 75275ed (branch-fix) fixup! ok
                    | * 2e85eb7 ok
                    |/
                    * b66353d init
                > git-auto-squash master
                Will only update "master", but leave "branch-fix" where it
                was. It results in:
                    * 0982b05 (master) Merge commit '75275ed'
                    |\
                    | * 377a349 ok
                    |/
                    * b66353d init
                With "-t" it also update ref "branch-fix" after squashing:
                > git-auto-squash -t master
                    * 0982b05 (master) Merge commit '75275ed'
                    |\
                    | * 377a349 (branch-fix) ok
                    |/
                    * b66353d init
                It is same with specifying which ref to update manually:
                > git-auto-squash -t master branch-fix
```

## 举个栗子

运行 `git-auto-squash` 后将所有 `fixup!` 开头的message的commit
合并到最早遇到的非`fixup!`的提交点"ok"上.

![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/git-auto-squash/51e34d0769a6a39b-example.png)

## 处理merge的栗子

`git-auto-squash` 也可以处理merge的fixup。对于merge
commit，如果它的其中一个parent被squash掉了，它也会被squash掉:

![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/git-auto-squash/0a8785639b9b1959-merge.png)

这样在某些merge commit有3个或3个以上的parent的时候，会丢弃某些中间的merge点。
但不影响最终结果。

处理merge的历史的时候建议加上`-t`参数，
以保证被重写的历史里所有的分支都会指向新的提交点。

## 下载

[git-auto-squash on gist](https://gist.github.com/drmingdrmer/2f7a2b9afdff6551208b)

复制脚本到/usr/local/bin下并:

```sh
chmod +x git-auto-squash
```



Reference:

