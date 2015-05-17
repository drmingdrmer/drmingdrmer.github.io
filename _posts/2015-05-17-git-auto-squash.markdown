---
layout: post
title:  "随手改变世界之 git-auto-squash"
date:   2015 May 17
categories: git
tags: util git auto squash filter-branch
---

使用git的同学是不是经常纠结于在开发过程中是应该频繁提交，
还是仔细构造提交点之后再提交？

-   前者可以让开发更流畅，不必打断思路，但会造成提交历史无法浏览；
-   后者可以构造漂亮易懂的提交历史，但码码时停下来考虑commit message
    怎么造句是不是太影响情绪了。

一般的做法是先做很多小的fixup，之后再将fixup合并到一起。

这个工具 `git-auto-squash` 可以将提交历史中连续的fixup
合并到它之前最早的1个正式提交点上，类似不需要交互的`rebase --interactive`。

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
```

## 举个栗子

运行 `git-auto-squash` 后将所有 `fixup!` 开头的message的commit
合并到最早遇到的非`fixup!`的提交点"ok"上.

![](/img/git-auto-squash/example.png)

## 下载

[git-auto-squash on gist](https://gist.github.com/drmingdrmer/2f7a2b9afdff6551208b)

复制脚本到/usr/local/bin下并:

```sh
chmod +x git-auto-squash
```
