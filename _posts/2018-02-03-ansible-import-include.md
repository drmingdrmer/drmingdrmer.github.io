---
layout:     post
title:      "ansible中的include, include_tasks 和 import_tasks 的差别"
date:       2018 Feb 03
categories: tech devops
tags:       ansible devops include include_tasks import_tasks
---

<!-- mdtoc start -->

- [include_tasks 和 import_tasks]({{page.url}}#includetasks-和-importtasks)
- [例子]({{page.url}}#例子)
    - [示例结果:]({{page.url}}#示例结果)


<!-- mdtoc end   -->


<a class="md-anchor" name="includetasks-和-importtasks"></a>

# include_tasks 和 import_tasks

<!--excerpt-->

`include` 被deprecated了. 建议使用`include_tasks` 和 `import_tasks`.

-   `include_tasks` 是动态的: 在运行时展开. when只应用一次.  被include的文件名可以使用变量.

-   `import_tasks` 是静态的: 在加载时展开. when在被import的文件里的每个task, 都会重新检查一次. 因为是加载时展开的, 文件名的变量不能是动态设定的.

    > When using static includes, ensure that any variables used in their names
    > are defined in vars/vars_files or extra-vars passed in from the command
    > line. Static includes cannot use variables from inventory sources like
    > group or host vars.

<!--more-->


<a class="md-anchor" name="例子"></a>

# 例子

`x.yml`:

```yaml
- hosts: 127.0.0.1
  gather_facts: False
  tasks:
    - set_fact: mode=1
    - include_tasks: y.yml
      when: mode == "1"

    - set_fact: mode=1
    - import_tasks: y.yml
      when: mode == "1"
```

`y.yml`:

```yaml
- set_fact: mode="2"

- debug:
    msg: >
      Display in only `include_tasks`.
      `include_tasks` does NOT re-evaluate `mode` for every step.
      `import_tasks` DOES re-evaluate condition.
```

运行`ansible-play -b x.yml` 后:
debug 的message只在`include_tasks` 里被执行了.

第2个`import_tasks`中的debug被skip掉了.

因为`mode`被改变之后, `include_tasks` 不会重新evaluate mode,`import_tasks`
会根据变化后的mode值重新evaluate每个task的条件.


<a class="md-anchor" name="示例结果"></a>

## 示例结果:

```
TASK [set_fact] *******************************************************
ok: [127.0.0.1]

TASK [include_tasks] **************************************************
included: /root/devops/ansible/y.yml for 127.0.0.1

TASK [set_fact] *******************************************************
ok: [127.0.0.1]

TASK [debug] **********************************************************
ok: [127.0.0.1] => {
    "msg": "Display in only `include_tasks`.
            `include_tasks` does NOT re-evaluate mode for every step.
            `import_tasks` DOES re-evaluate condition\n"
}

TASK [set_fact] *******************************************************
ok: [127.0.0.1]

TASK [set_fact] *******************************************************
ok: [127.0.0.1]

TASK [debug] **********************************************************
skipping: [127.0.0.1]
```
