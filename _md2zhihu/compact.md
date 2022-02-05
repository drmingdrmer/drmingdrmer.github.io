
# 问题

系统中的所有数据以block 存放: 每个block里:

-   有 `n`=1000万个文件, 已经排序好,
-   每个文件名长度平均`l`=512 Byte.

2个block中可能包含大量的重复文件, 这时我们需要找出这2个block, 将其合并,
以节省空间.

问题: 如何高效的(在时间上和空间上) 找出具有大量重复文件的block对.

问题包含2个部分:

-   创建数据结构保存在block中, 作为 **签名**
-   在需要时对比2个block的签名以得出 **相似度**

# 常规方法

## 1. 文件列表

因为block内的文件名是排序的, 可以直接对比2个block各自的文件列表,
走一遍归并, 这样,

### 创建签名的开销:

-   时间和空间开销: `O(n x l)`, 每个block需要存储: 5G 数据: 1000万 x 512

### 计算相似度的开销:

-   总的时间复杂度是`O(n x l)`, 需要读取  5G x 2的数据

这种方法可以非常准确的得出重复文件数量. 但空间开销和时间开销都比较大.

## 2. hash-bitmap

另外一个直接的, 近似的方案是使用hash-bitmap:

### 创建签名:

对每个block, 将所有文件名做1次hash,
例如: `int(sha1(fn)) % b`,
这里b 是bitmap的大小, 如果取b=64 * 10^6, 这个hash 表是比较稀疏的(n/b=0.16),
冲突率也就比较低, 大约有7%的冲突率, 参考: [hash-collision](http://drmingdrmer.github.io/math/hash/2017/08/05/numbers-programmers-should-know-about-hash-zh.html#%E6%AF%8F%E7%B1%BBbucket%E7%9A%84%E6%95%B0%E9%87%8F)

### 计算相似度:

然后再对比2个block的时候, 可以通过将2个bitmap取`AND`操作,
找到存在于2个block中的bit有几个, 来确定重复的文件数.

### 这种方法是粗略的估计:

-   其一是hash时, 在同一个block中, 2个fn的hash可能落到1个bit上, 导致不准确.

-   其二是2个block中把不同的fn也可能hash到1个bit上,
    导致估算时增加重复文件的统计.

### 创建签名的开销:

-   空间复杂度: `O(n)`, 实际存储空间开销是 8MB,
    因为不同的block的bitmap大小必须一致, 所以要取最大可能的大小.

-   时间复杂度是 `O(n x l)`

### 计算相似度的开销:

-   时间复杂度是 `O(n/64)`, 因为目标机器是64位的,
    位AND操作一次可以对比64个bit(1个`int64_t`)

但这2个方案都不是最好的, 虽然hash-bitmap的方案空间开销已经很小了.

接下来我们看看这个思路: min-hash

# 方案: min-hash

[min-hash](https://en.wikipedia.org/wiki/MinHash) 实现了使用常量的空间开销对2个集合进行相似度的比较.

## 原理

-   A, B 是2个集合, 我们定义一个相似度的函数: Jaccard-similarity:
    `J(A, B) = len(A ∩ B) / len(A ∪ B)`

-   假设有1个hash函数, 它不会对不同的输入得出相同的hash值, 即:
    如果`x != y`, 那么`hash(x) != hash(y)`,
    这里我们在测试演示的时候就选择用`sha1`了,
    而且将sha1的输出结果按照16进制40位整数处理.

-   最小hash值: 一个集合S中所有元素的hash值最小的那个(hash值, 不是原始元素),
    对我们的场景来说:

    ```
    min_a = min([ sha1(x) for x in A ])
    min_b = min([ sha1(x) for x in B ])
    ```

显然如果A和B的元素一样, 那么`min_a == min_b`;

如果A和B的元素有很多重复, 那么`min_a` 和 `min_b`有很大概率相同;

更精确的, 对A, B两个集合,
**min_a == min_b 的概率是 J = len(A ∩ B) / len(A ∪ B)**

### 解释下上面的结论的推导过程

-   对有n个元素的集合S, 假设S集合未知, 也就是说它里面的元素都是随机的,
    那么, 对其中所有元素做一次hash后, 其中的一个元素e, 成为最小hash的概率是`1/n`,
    也就是: `P(sha1(e) == min([ sha1(x) for x in S ])) = 1/n`

    > 因为假设hash函数均匀, 每个元素成为最小元素的几率都是相等的.


-   对于要对比的2个集合A和B, 元素共有: `A ∪ B`,
    取`min_ab = min([ hash(x) for x in (A ∪ B) ])`,
    `A ∪ B`中每个元素成为`min_ab`的几率是 `1 / len(A ∪ B)`

    因此`A ∩ B`里的一个元素e 成为`min_ab` 的几率是`len(A ∩ B) / len(A ∪ B)`.

-   而`A ∩ B`里的一个元素e 成为`min_ab`, 是 `min_a == min_b` 的充要条件.

    所以有
    **`P(min_a == min_b) = J = len(A ∩ B) / len(A ∪ B)`**

所以我们的问题就转化成:
**求出P, 我们就知道的2个block中重复文件的比例J**

使用 min-hash 求相似度的步骤也是2个:

### 生成签名:

-   确定一个hash函数, 测试中就用`sha1`了.

-   分别为A 和 B准备`b`个bucket: `bucket_a` 和 `bucket_b`.

-   对A中所有元素计算sha1, 按照`sha1(a) % b`拆分A中的元素到b个bucket中:

    `bucket_a[sha1(a) % b].append(sha1(a))`

    对B也做同样的操作.

-   记录A, B中每个bucket中的最小hash值:

    ```
    for i in range(0, b):
        bucket_a[i] = min(bucket_a[i])
        bucket_b[i] = min(bucket_b[i])

    ```

> 将元素分散到b个bucket中, 是为了通过概率的均值来估算概率P.
> 这里也暗含了一个假设: bucket_a[i] 中的元素与bucket_b[i]的元素相似度与 `len(A ∩ B) / len(A ∪ B)` 相近
> 因为假设认为sha1 非常随机地分散了A或B中的元素, 子集相似度接近全集相似度.


### 计算相似度:

对比2个block, 统计`min_a == min_b`的个数:

```
eq = 0.0
for i in range(0, b):
    if bucket_a[i] == bucket_b[i]:
        eq += 1
P = eq / b
```

因为P == J, 所以我们就得到了2个block的相似度.

## min-hash 实现

实现时, 要求对比的2个block的使用的bucket数量`b`相同.

-   空间复杂度 `O(b)`: `1KB = sizeof(int64) * b` `b=128`
-   时间复杂度: `O(b)`: 128次int 比较

通过min-hash 计算相似度 和 对比真实统计相似度的python代码: [min-hash.py](/post-res/compact/min-hash.py)

通过这个程序模拟的结果如下:

## 模拟验证

NO. bucket: 128

Hash length: int64

<table>
<tr class="header">
<th style="text-align: right;">总数</th>
<th style="text-align: right;">a总数</th>
<th style="text-align: right;">b总数</th>
<th style="text-align: right;">实际重复率(A∩B)/(A∪B)%</th>
<th style="text-align: right;">估算重复%</th>
<th style="text-align: right;">误差%</th>
</tr>
<tr class="odd">
<td style="text-align: right;">1000</td>
<td style="text-align: right;">360</td>
<td style="text-align: right;">840</td>
<td style="text-align: right;">20.00%</td>
<td style="text-align: right;">21.88%</td>
<td style="text-align: right;">1.87%</td>
</tr>
<tr class="even">
<td style="text-align: right;">1000</td>
<td style="text-align: right;">520</td>
<td style="text-align: right;">880</td>
<td style="text-align: right;">40.00%</td>
<td style="text-align: right;">38.28%</td>
<td style="text-align: right;">-1.72%</td>
</tr>
<tr class="odd">
<td style="text-align: right;">1000</td>
<td style="text-align: right;">680</td>
<td style="text-align: right;">920</td>
<td style="text-align: right;">60.00%</td>
<td style="text-align: right;">60.94%</td>
<td style="text-align: right;">0.94%</td>
</tr>
<tr class="even">
<td style="text-align: right;">1000</td>
<td style="text-align: right;">839</td>
<td style="text-align: right;">959</td>
<td style="text-align: right;">80.16%</td>
<td style="text-align: right;">78.91%</td>
<td style="text-align: right;">-1.25%</td>
</tr>
<tr class="odd">
<td style="text-align: right;">1000</td>
<td style="text-align: right;">1000</td>
<td style="text-align: right;">1000</td>
<td style="text-align: right;">100.00%</td>
<td style="text-align: right;">100.00%</td>
<td style="text-align: right;">0.00%</td>
</tr>
<tr class="even">
<td style="text-align: right;">10000</td>
<td style="text-align: right;">3600</td>
<td style="text-align: right;">8400</td>
<td style="text-align: right;">20.00%</td>
<td style="text-align: right;">15.62%</td>
<td style="text-align: right;">-4.38%</td>
</tr>
<tr class="odd">
<td style="text-align: right;">10000</td>
<td style="text-align: right;">5200</td>
<td style="text-align: right;">8800</td>
<td style="text-align: right;">40.00%</td>
<td style="text-align: right;">35.16%</td>
<td style="text-align: right;">-4.84%</td>
</tr>
<tr class="even">
<td style="text-align: right;">10000</td>
<td style="text-align: right;">6800</td>
<td style="text-align: right;">9200</td>
<td style="text-align: right;">60.00%</td>
<td style="text-align: right;">60.94%</td>
<td style="text-align: right;">0.94%</td>
</tr>
<tr class="odd">
<td style="text-align: right;">10000</td>
<td style="text-align: right;">8399</td>
<td style="text-align: right;">9599</td>
<td style="text-align: right;">80.02%</td>
<td style="text-align: right;">85.16%</td>
<td style="text-align: right;">5.14%</td>
</tr>
<tr class="even">
<td style="text-align: right;">10000</td>
<td style="text-align: right;">10000</td>
<td style="text-align: right;">10000</td>
<td style="text-align: right;">100.00%</td>
<td style="text-align: right;">100.00%</td>
<td style="text-align: right;">0.00%</td>
</tr>
<tr class="odd">
<td style="text-align: right;">100000</td>
<td style="text-align: right;">36000</td>
<td style="text-align: right;">84000</td>
<td style="text-align: right;">20.00%</td>
<td style="text-align: right;">21.88%</td>
<td style="text-align: right;">1.87%</td>
</tr>
<tr class="even">
<td style="text-align: right;">100000</td>
<td style="text-align: right;">52000</td>
<td style="text-align: right;">88000</td>
<td style="text-align: right;">40.00%</td>
<td style="text-align: right;">47.66%</td>
<td style="text-align: right;">7.66%</td>
</tr>
<tr class="odd">
<td style="text-align: right;">100000</td>
<td style="text-align: right;">68000</td>
<td style="text-align: right;">92000</td>
<td style="text-align: right;">60.00%</td>
<td style="text-align: right;">62.50%</td>
<td style="text-align: right;">2.50%</td>
</tr>
<tr class="even">
<td style="text-align: right;">100000</td>
<td style="text-align: right;">83999</td>
<td style="text-align: right;">95999</td>
<td style="text-align: right;">80.00%</td>
<td style="text-align: right;">80.47%</td>
<td style="text-align: right;">0.47%</td>
</tr>
<tr class="odd">
<td style="text-align: right;">100000</td>
<td style="text-align: right;">100000</td>
<td style="text-align: right;">100000</td>
<td style="text-align: right;">100.00%</td>
<td style="text-align: right;">100.00%</td>
<td style="text-align: right;">0.00%</td>
</tr>
<tr class="even">
<td style="text-align: right;">1000000</td>
<td style="text-align: right;">360000</td>
<td style="text-align: right;">840000</td>
<td style="text-align: right;">20.00%</td>
<td style="text-align: right;">19.53%</td>
<td style="text-align: right;">-0.47%</td>
</tr>
<tr class="odd">
<td style="text-align: right;">1000000</td>
<td style="text-align: right;">520000</td>
<td style="text-align: right;">880000</td>
<td style="text-align: right;">40.00%</td>
<td style="text-align: right;">40.62%</td>
<td style="text-align: right;">0.62%</td>
</tr>
<tr class="even">
<td style="text-align: right;">1000000</td>
<td style="text-align: right;">680000</td>
<td style="text-align: right;">920000</td>
<td style="text-align: right;">60.00%</td>
<td style="text-align: right;">58.59%</td>
<td style="text-align: right;">-1.41%</td>
</tr>
<tr class="odd">
<td style="text-align: right;">1000000</td>
<td style="text-align: right;">839999</td>
<td style="text-align: right;">959999</td>
<td style="text-align: right;">80.00%</td>
<td style="text-align: right;">75.78%</td>
<td style="text-align: right;">-4.22%</td>
</tr>
<tr class="even">
<td style="text-align: right;">1000000</td>
<td style="text-align: right;">1000000</td>
<td style="text-align: right;">1000000</td>
<td style="text-align: right;">100.00%</td>
<td style="text-align: right;">100.00%</td>
<td style="text-align: right;">0.00%</td>
</tr>
</table>

# 结论

<!--excerpt-->

系统中的所有数据以block 存放,
2个block中可能包含大量的重复文件, 这时我们需要找出这2个block, 将其合并,

问题: 如何高效的(在时间上和空间上) 找出具有大量重复文件的block对.

假设:

-   每个block的文件数 `n = 1000万`
-   单个文件名长度: `l = 512 字节`
-   hash-bitmap 大小 `64 * 10^6 = 8MB`
-   min-hash bucket数量 `b = 128`

各种算法的开销如下

<table>
<tr class="header">
<th style="text-align: left;">算法</th>
<th style="text-align: left;">空间开销</th>
<th style="text-align: left;">实际空间</th>
<th style="text-align: left;">时间开销</th>
</tr>
<tr class="odd">
<td style="text-align: left;">fn-list</td>
<td style="text-align: left;">O(n x l)</td>
<td style="text-align: left;">5GB</td>
<td style="text-align: left;">O(n x l)</td>
</tr>
<tr class="even">
<td style="text-align: left;">hash-bitmap</td>
<td style="text-align: left;">O(n)</td>
<td style="text-align: left;">8MB</td>
<td style="text-align: left;">O(n)</td>
</tr>
<tr class="odd">
<td style="text-align: left;">min-hash</td>
<td style="text-align: left;">O(1)</td>
<td style="text-align: left;">1KB</td>
<td style="text-align: left;">O(1)</td>
</tr>
</table>

<!--more-->

# 参考:

-   [min-hash](https://en.wikipedia.org/wiki/MinHash)

-   [hash-collision 计算方式](http://drmingdrmer.github.io/math/hash/2017/08/05/numbers-programmers-should-know-about-hash-zh.html#%E6%AF%8F%E7%B1%BBbucket%E7%9A%84%E6%95%B0%E9%87%8F)



Reference:

- hash-collision : [http://drmingdrmer.github.io/math/hash/2017/08/05/numbers-programmers-should-know-about-hash-zh.html#%E6%AF%8F%E7%B1%BBbucket%E7%9A%84%E6%95%B0%E9%87%8F](http://drmingdrmer.github.io/math/hash/2017/08/05/numbers-programmers-should-know-about-hash-zh.html#%E6%AF%8F%E7%B1%BBbucket%E7%9A%84%E6%95%B0%E9%87%8F)

- min-hash : [https://en.wikipedia.org/wiki/MinHash](https://en.wikipedia.org/wiki/MinHash)


[hash-collision]:  http://drmingdrmer.github.io/math/hash/2017/08/05/numbers-programmers-should-know-about-hash-zh.html#%E6%AF%8F%E7%B1%BBbucket%E7%9A%84%E6%95%B0%E9%87%8F
[min-hash]:  https://en.wikipedia.org/wiki/MinHash