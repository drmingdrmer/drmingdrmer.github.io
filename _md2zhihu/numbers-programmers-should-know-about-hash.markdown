
There is a hash table:

-   It has `b` buckets.
-   It has `n` keys stored in it.
-   We assume that the hash function distributes keys uniformly.
-   A bucket can contain more than 1 keys.

If `n` <img src="https://www.zhihu.com/equation?tex=%20%5Capprox%20" alt=" \approx " class="ee_img tr_noresize" eeimg="1"> `b`, the hash table would look like this:

-   **37%** buckets are empty.
-   **37%** buckets contain 1 key.
-   **26%** buckets contain more than 1 key, which means collision occurs.

The following chart created by program simulation shows distribution of 20 keys
over 20 buckets.

![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/numbers-programmers-should-know-about-hash/5866d5812ab7bf05-dist-1-with-label.png)

<!--more-->

### Load Factor and Key Distribution

Let `load factor` <img src="https://www.zhihu.com/equation?tex=%20%5Calpha%20" alt=" \alpha " class="ee_img tr_noresize" eeimg="1"> be: <img src="https://www.zhihu.com/equation?tex=%20%5Calpha%20%3D%20%5Cfrac%7Bn%7D%7Bb%7D%20" alt=" \alpha = \frac{n}{b} " class="ee_img tr_noresize" eeimg="1">.
`load factor` defines almost everything in a hash table.

### Load Factor 
`<0.75`

Normally in-memory hash table implementations keep `load factor` lower than
**0.75**.
This makes collision rate relatively low, thus looking up is very fast.
The lower the collision rate is, the less the time it takes to resolve collision,
since [linear-probing](http://en.wikipedia.org/wiki/Linear_probing) is normally used and it is very sensitive to collision
rate.

In this case, there are about **47%** buckets empty. And nearly half of these
47% will be used again by [linear-probing](http://en.wikipedia.org/wiki/Linear_probing).

As we can see from the first chart, when `load factor` is small, key
distribution is very uneven. What we need to know is how `load factor` affects
key distribution.

Increasing `load factor` would reduce the number of empty buckets and increase
the collision rate. It is monotonic but not linear, as the following table and
the picture shows:

#### Load factor, empty buckets, buckets having 1 key and buckets having more than 1 keys:

<table>
<tr class="header">
<th style="text-align: left;">load factor(n/b)</th>
<th style="text-align: right;">0</th>
<th style="text-align: right;">1</th>
<th style="text-align: right;">&gt;1</th>
</tr>
<tr class="odd">
<td style="text-align: left;">0.5</td>
<td style="text-align: right;">61%</td>
<td style="text-align: right;">30%</td>
<td style="text-align: right;">9%</td>
</tr>
<tr class="even">
<td style="text-align: left;">0.75</td>
<td style="text-align: right;">47%</td>
<td style="text-align: right;">35%</td>
<td style="text-align: right;">17%</td>
</tr>
<tr class="odd">
<td style="text-align: left;"><strong>1.0</strong></td>
<td style="text-align: right;">37%</td>
<td style="text-align: right;">37%</td>
<td style="text-align: right;">26%</td>
</tr>
<tr class="even">
<td style="text-align: left;">2.0</td>
<td style="text-align: right;">14%</td>
<td style="text-align: right;">27%</td>
<td style="text-align: right;">59%</td>
</tr>
<tr class="odd">
<td style="text-align: left;">5.0</td>
<td style="text-align: right;">01%</td>
<td style="text-align: right;">03%</td>
<td style="text-align: right;">96%</td>
</tr>
<tr class="even">
<td style="text-align: left;">10.0</td>
<td style="text-align: right;">00%</td>
<td style="text-align: right;">00%</td>
<td style="text-align: right;">100%</td>
</tr>
</table>

![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/numbers-programmers-should-know-about-hash/82ded63f1c56e284-load-factor-empty-collision.png)

> **0.75** has been chosen as upper limit of `load factor` not only because
> of concerns of collision rate, but also because of the way [linear-probing](http://en.wikipedia.org/wiki/Linear_probing)
> works. But that is ultimately irrelevant.


### Tips

-   It is **impossible** to use hash tables with low space overload and at the
    same time, with low collision rate.

    -   The truth is that just enough buckets waste **37%** space.

-   Use hash tables only for (in memory) small data sets.

-   High level languages like Java and Python have builtin hash tables that keep
    `load factor` below **0.75**.

-   Hash tables do **NOT** uniformly distribute small sets of keys over all
    buckets.

### Load Factor 
`>1.0`

When `load factor` is greater than `1.0`, [linear-probing](http://en.wikipedia.org/wiki/Linear_probing) can not work any
more, since there are not enough buckets for all keys. [chaining](http://en.wikipedia.org/wiki/Hash_table#Separate_chaining) keys in a
single bucket with [linked-list](http://en.wikipedia.org/wiki/Linked_list) is a practical method to resolve collision.

[linked-list](http://en.wikipedia.org/wiki/Linked_list) works well only when `load factor` is not very large, since
[linked-list](http://en.wikipedia.org/wiki/Linked_list) operation has `O(n)` time complexity.
For very large `load factor` [tree](http://en.wikipedia.org/wiki/Tree_(ata_structure)) or similar data structure should be considered.

### Load Factor 
`>10.0`

When `load factor` becomes very large, the probability that a bucket is empty
converges to 0. And the key distribution converges to the average.

### The higher 
`load factor`
 is, the more uniformly keys are distributed

Let the average number of keys in each bucket be:

<img src="https://www.zhihu.com/equation?tex=%20%7Bavg%7D%20%3D%20%5Cfrac%7Bn%7D%7Bb%7D%20%5C%5C" alt=" {avg} = \frac{n}{b} \\" class="ee_img tr_noresize" eeimg="1">

`100%` means a bucket contains exactly <img src="https://www.zhihu.com/equation?tex=%20%7Bavg%7D%20" alt=" {avg} " class="ee_img tr_noresize" eeimg="1"> keys.
The following charts show what distribution is like when `load factor` is **10**,
**100** and **1000**:

![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/numbers-programmers-should-know-about-hash/ff934b2b0dc9cad3-dist-10.png)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/numbers-programmers-should-know-about-hash/36f0393747176629-dist-100.png)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/numbers-programmers-should-know-about-hash/082c8fc0c0a1c070-dist-1000.png)

As `load factor` becomes higher, the gap between the most keys and the fewest
keys becomes smaller.

<table>
<tr class="header">
<th style="text-align: right;">load factor</th>
<th style="text-align: right;">(most-fewest)/most</th>
<th style="text-align: right;">fewest</th>
</tr>
<tr class="odd">
<td style="text-align: right;">1</td>
<td style="text-align: right;">100.0%</td>
<td style="text-align: right;">0</td>
</tr>
<tr class="even">
<td style="text-align: right;">10</td>
<td style="text-align: right;">88.0%</td>
<td style="text-align: right;">2</td>
</tr>
<tr class="odd">
<td style="text-align: right;">100</td>
<td style="text-align: right;">41.2%</td>
<td style="text-align: right;">74</td>
</tr>
<tr class="even">
<td style="text-align: right;">1,000</td>
<td style="text-align: right;">15.5%</td>
<td style="text-align: right;">916</td>
</tr>
<tr class="odd">
<td style="text-align: right;">10,000</td>
<td style="text-align: right;">5.1%</td>
<td style="text-align: right;">9735</td>
</tr>
<tr class="even">
<td style="text-align: right;">100,000</td>
<td style="text-align: right;">1.6%</td>
<td style="text-align: right;">99161</td>
</tr>
</table>

### Calculation

Most of the numbers from above are produced by program simulations.
From this chapter we are going to see what the distribution is in math.

#### Expected number of each kind of buckets:

-   `0` key: <img src="https://www.zhihu.com/equation?tex=%20b%20e%5E%7B-%5Cfrac%7Bn%7D%7Bb%7D%7D%20" alt=" b e^{-\frac{n}{b}} " class="ee_img tr_noresize" eeimg="1">
-   `1` key: <img src="https://www.zhihu.com/equation?tex=%20n%20e%5E%7B%20-%20%5Cfrac%7Bn%7D%7Bb%7D%20%7D%20" alt=" n e^{ - \frac{n}{b} } " class="ee_img tr_noresize" eeimg="1">
-   `>1` key: <img src="https://www.zhihu.com/equation?tex=%20b%20-%20b%20e%5E%7B-%5Cfrac%7Bn%7D%7Bb%7D%7D%20-%20n%20e%5E%7B%20-%20%5Cfrac%7Bn%7D%7Bb%7D%20%7D%20" alt=" b - b e^{-\frac{n}{b}} - n e^{ - \frac{n}{b} } " class="ee_img tr_noresize" eeimg="1">

### Number of Empty Buckets

The chance a certain key is **NOT** in a certain bucket is:
<img src="https://www.zhihu.com/equation?tex=%20%5Cfrac%7Bb-1%7D%7Bb%7D%20" alt=" \frac{b-1}{b} " class="ee_img tr_noresize" eeimg="1">.
Since: <img src="https://www.zhihu.com/equation?tex=%20%5Clim_%7Bb%5Cto%20%5Cinfty%7D%20%281%2B%5Cfrac%7B1%7D%7Bb%7D%29%5Eb%20%3D%20e%20" alt=" \lim_{b\to \infty} (1+\frac{1}{b})^b = e " class="ee_img tr_noresize" eeimg="1">.
The probability of a certain bucket being empty is:

<img src="https://www.zhihu.com/equation?tex=%28%5Cfrac%7Bb-1%7D%7Bb%7D%29%5En%20%3D%20%28%281-%20%5Cfrac%7B1%7Db%29%5Eb%29%5E%7B%5Cfrac%7Bn%7D%7Bb%7D%7D%20%3D%20e%5E%7B-%5Cfrac%7Bn%7D%7Bb%7D%7D%5C%5C" alt="(\frac{b-1}{b})^n = ((1- \frac{1}b)^b)^{\frac{n}{b}} = e^{-\frac{n}{b}}\\" class="ee_img tr_noresize" eeimg="1">

Thus the total number of empty buckets is:

<img src="https://www.zhihu.com/equation?tex=%20b%20e%5E%7B-%5Cfrac%7Bn%7D%7Bb%7D%7D%20%5C%5C" alt=" b e^{-\frac{n}{b}} \\" class="ee_img tr_noresize" eeimg="1">

### Number of Buckets Having 1 Key

The probability of a bucket having exactly 1 key is:

<img src="https://www.zhihu.com/equation?tex=%7Bn%20%5Cchoose%201%7D%20%28%20%5Cfrac%7B1%7D%7Bb%7D%20%29%5E1%20%28%201%20-%20%5Cfrac%7B1%7D%7Bb%7D%20%29%5E%7Bn-1%7D%20%3D%20%5Cfrac%7Bn%7D%7Bb%7D%20e%5E%7B-%5Cfrac%7Bn%7D%7Bb%7D%7D%5C%5C" alt="{n \choose 1} ( \frac{1}{b} )^1 ( 1 - \frac{1}{b} )^{n-1} = \frac{n}{b} e^{-\frac{n}{b}}\\" class="ee_img tr_noresize" eeimg="1">

> One of the `n` keys is in this bucket, and at the same time, no other key
> is in this bucket:


The the number of buckets having exactly 1 key is:

<img src="https://www.zhihu.com/equation?tex=%20b%5Cfrac%7Bn%7D%7Bb%7D%20e%5E%7B-%5Cfrac%7Bn%7D%7Bb%7D%7D%20%3D%20n%20e%5E%7B%20-%20%5Cfrac%7Bn%7D%7Bb%7D%20%7D%20%5C%5C" alt=" b\frac{n}{b} e^{-\frac{n}{b}} = n e^{ - \frac{n}{b} } \\" class="ee_img tr_noresize" eeimg="1">

### Number of Buckets Having More Than One Key

<img src="https://www.zhihu.com/equation?tex=%20b%20-%20b%20e%5E%7B-%5Cfrac%7Bn%7D%7Bb%7D%7D%20-%20n%20e%5E%7B%20-%20%5Cfrac%7Bn%7D%7Bb%7D%20%7D%20%5C%5C" alt=" b - b e^{-\frac{n}{b}} - n e^{ - \frac{n}{b} } \\" class="ee_img tr_noresize" eeimg="1">

### Distribution Uniformity

Similarly, the probability of a bucket having exactly `i` keys is:

<img src="https://www.zhihu.com/equation?tex=p%28i%29%20%3D%20%7Bn%20%5Cchoose%20i%7D%20%28%20%5Cfrac%7B1%7D%7Bb%7D%20%29%5E%7B%20i%20%7D%20%28%201%20-%20%5Cfrac%7B1%7D%7Bb%7D%20%29%5E%7Bn-i%7D%5C%5C" alt="p(i) = {n \choose i} ( \frac{1}{b} )^{ i } ( 1 - \frac{1}{b} )^{n-i}\\" class="ee_img tr_noresize" eeimg="1">

The probability distribution is [binomial-distribution](http://en.wikipedia.org/wiki/Binomial_distribution).

And we want to know how many keys there are in the bucket having the fewest keys
and in the bucket having the most keys.

### Approximation by Normal Distribution

When `n` and `b` are large, [binomial-distribution](http://en.wikipedia.org/wiki/Binomial_distribution) can be approximated by
[normal-distribution](http://en.wikipedia.org/wiki/Normal_distribution) to estimate uniformity.

Let <img src="https://www.zhihu.com/equation?tex=%20p%20%3D%20%5Cfrac%7B1%7D%7Bb%7D%20" alt=" p = \frac{1}{b} " class="ee_img tr_noresize" eeimg="1">. The probability of a bucket having exactly `i`
keys is:

<img src="https://www.zhihu.com/equation?tex=p%28i%29%20%3D%20%7Bn%20%5Cchoose%20i%7Dp%5Ei%281-p%29%5E%7Bn-i%7D%5Capprox%20%5Cfrac%7B1%7D%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%5Csigma%20%5Csqrt%7B2%20%5Cpi%7D%20%7D%20%20%20%20%20%20%20%20e%5E%7B%20-%20%5Cfrac%7B%28i-%5Cmu%29%5E2%7D%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B2%20%5Csigma%5E2%7D%20%7D%5C%5C" alt="p(i) = {n \choose i}p^i(1-p)^{n-i}\approx \frac{1}             {\sigma \sqrt{2 \pi} }        e^{ - \frac{(i-\mu)^2}                   {2 \sigma^2} }\\" class="ee_img tr_noresize" eeimg="1">

Where:

<img src="https://www.zhihu.com/equation?tex=%5Cmu%20%3D%20np%20%5C%5C%5Csigma%5E2%20%3D%20np%281-p%29%20%5C%5C%5C%5C" alt="\mu = np \\\sigma^2 = np(1-p) \\\\" class="ee_img tr_noresize" eeimg="1">

The probability that a bucket has **less** than `x` keys is:

<img src="https://www.zhihu.com/equation?tex=P%28x%29%20%3D%20%5Csum_%7Bi%3D0%7D%5Ex%20p%28i%29%5C%5C" alt="P(x) = \sum_{i=0}^x p(i)\\" class="ee_img tr_noresize" eeimg="1">

Thus in this hash table, the total number of buckets having less than `x` keys is:

<img src="https://www.zhihu.com/equation?tex=b%20%5Ccdot%20P%28x%29%20%3D%20b%20%5Ccdot%20%5Csum_%7Bi%3D0%7D%5Ex%20p%28i%29%5C%5C" alt="b \cdot P(x) = b \cdot \sum_{i=0}^x p(i)\\" class="ee_img tr_noresize" eeimg="1">

Choose `x` so that the total number of such buckets is `1`. Then this only
bucket must be the one that has the fewest keys. So find `x` that satisfies:

<img src="https://www.zhihu.com/equation?tex=b%20%5Ccdot%20%5Csum_%7Bi%3D0%7D%5Ex%20p%28i%29%20%3D%201%5C%5C" alt="b \cdot \sum_{i=0}^x p(i) = 1\\" class="ee_img tr_noresize" eeimg="1">

With this `x`, the expected number of keys in this bucket is:

<img src="https://www.zhihu.com/equation?tex=N_%7Bmin%7D%20%3D%5Cfrac%7B%20%5Csum_%7Bi%3D0%7D%5Ex%20i%20%5Ccdot%20p%28i%29%20%7D%20%20%20%20%20%7B%20%5Csum_%7Bi%3D0%7D%5Ex%20p%28i%29%20%7D%3D%20b%20%5Ccdot%20%5Csum_%7Bi%3D0%7D%5Ex%20i%20%5Ccdot%20p%28i%29%5Capprox%20b%20%5Cint_%7Bi%3D0%7D%5Ex%20i%20%5Ccdot%20p%28i%29%20di%5C%5C" alt="N_{min} =\frac{ \sum_{i=0}^x i \cdot p(i) }     { \sum_{i=0}^x p(i) }= b \cdot \sum_{i=0}^x i \cdot p(i)\approx b \int_{i=0}^x i \cdot p(i) di\\" class="ee_img tr_noresize" eeimg="1">

Since normal distribution is symmetric:

<img src="https://www.zhihu.com/equation?tex=N_%7Bmax%7D%20%2B%20N_%7Bmin%7D%20%3D%202%20%5Cmu%20%3D%202%20%5Cfrac%7Bn%7D%7Bb%7D%5C%5C" alt="N_{max} + N_{min} = 2 \mu = 2 \frac{n}{b}\\" class="ee_img tr_noresize" eeimg="1">

### Find 
`x`

Now what we need to do is to find `x` in order to find
<img src="https://www.zhihu.com/equation?tex=%20N_%7Bmax%7D%20" alt=" N_{max} " class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=%20%5C%20N_%7Bmin%7D%20" alt=" \ N_{min} " class="ee_img tr_noresize" eeimg="1">.

The probability of a bucket that contains less than `x` keys is:

<img src="https://www.zhihu.com/equation?tex=%5Csum_%7Bi%3D0%7D%5Ex%20p%28i%29%5Capprox%20%5Cint_%7B0%7D%5E%7Bx%7D%20p%28i%29%20di%5Capprox%20%5Cint_%7B-%5Cinfty%7D%5E%7Bx%7D%20p%28i%29%20di%3D%20%5CPhi%28%20%5Cfrac%7Bx-%5Cmu%7D%5Csigma%20%29%5C%5C" alt="\sum_{i=0}^x p(i)\approx \int_{0}^{x} p(i) di\approx \int_{-\infty}^{x} p(i) di= \Phi( \frac{x-\mu}\sigma )\\" class="ee_img tr_noresize" eeimg="1">

<img src="https://www.zhihu.com/equation?tex=%20%5CPhi%28x%29%20%5C%5C" alt=" \Phi(x) \\" class="ee_img tr_noresize" eeimg="1">
is [cdf](http://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function) of standard normal distribution. When `x - u` is close to `0`, it is
approximated by:

$$
\Phi(x); =;0.5+\frac{1}{\sqrt{2\pi}}\cdot e^{-x^2/2}\left[x+\frac{x^3}{3}+\frac{x^5}{3\cdot 5}+\cdots+\frac{x^{2n+1}}{(2n+1)!!} + \cdots\right]
$$

By iterating `x` backward from `u` to `0`, we can find the solution to

<img src="https://www.zhihu.com/equation?tex=%20b%20%5Ccdot%20%5CPhi%28%5Cfrac%7Bx-%5Cmu%7D%5Csigma%29%20%3D%201%20%5C%5C" alt=" b \cdot \Phi(\frac{x-\mu}\sigma) = 1 \\" class="ee_img tr_noresize" eeimg="1">

Using this `x` we can find <img src="https://www.zhihu.com/equation?tex=%20N_%7Bmin%7D%20" alt=" N_{min} " class="ee_img tr_noresize" eeimg="1"> and <img src="https://www.zhihu.com/equation?tex=%20N_%7Bmax%7D%20" alt=" N_{max} " class="ee_img tr_noresize" eeimg="1">.

### Simulations in Python

Several simulation programs used in this post are here:
[hash-simulation](https://gist.github.com/drmingdrmer/f94b945cf7d5f287eb78)

### Reference

-   [linear-probing](http://en.wikipedia.org/wiki/Linear_probing)
-   [double-hash](http://en.wikipedia.org/wiki/Double_hashing)
-   [normal-distribution](http://en.wikipedia.org/wiki/Normal_distribution)
-   [binomial-distribution](http://en.wikipedia.org/wiki/Binomial_distribution)
-   [cdf](http://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function)



Reference:

- binomial-distribution : [http://en.wikipedia.org/wiki/Binomial_distribution](http://en.wikipedia.org/wiki/Binomial_distribution)

- cdf : [http://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function](http://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function)

- chaining : [http://en.wikipedia.org/wiki/Hash_table#Separate_chaining](http://en.wikipedia.org/wiki/Hash_table#Separate_chaining)

- double-hash : [http://en.wikipedia.org/wiki/Double_hashing](http://en.wikipedia.org/wiki/Double_hashing)

- linear-probing : [http://en.wikipedia.org/wiki/Linear_probing](http://en.wikipedia.org/wiki/Linear_probing)

- linked-list : [http://en.wikipedia.org/wiki/Linked_list](http://en.wikipedia.org/wiki/Linked_list)

- normal-distribution : [http://en.wikipedia.org/wiki/Normal_distribution](http://en.wikipedia.org/wiki/Normal_distribution)

- tree : [http://en.wikipedia.org/wiki/Tree_(ata_structure)](http://en.wikipedia.org/wiki/Tree_(ata_structure))


[binomial-distribution]:  http://en.wikipedia.org/wiki/Binomial_distribution
[cdf]:  http://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function
[chaining]:  http://en.wikipedia.org/wiki/Hash_table#Separate_chaining
[double-hash]:  http://en.wikipedia.org/wiki/Double_hashing
[linear-probing]:  http://en.wikipedia.org/wiki/Linear_probing
[linked-list]:  http://en.wikipedia.org/wiki/Linked_list
[normal-distribution]:  http://en.wikipedia.org/wiki/Normal_distribution
[tree]:  http://en.wikipedia.org/wiki/Tree_(ata_structure)