---
layout: post
title:  "Numbers Programmers Should Know About Hash"
date:   2015 Feb 17
categories: math hash
tags: hash collision math
---

There is a hash table:

*   It has `b` buckets.
*   It has `n` keys stored in it.
*   We assume that the hash function distributes keys uniformly.
*   A bucket is able to contain more than one key.

If `n` $$ \approx $$ `b`, the hash table would look like this:

*   **37%** buckets are empty.
*   **37%** buckets contain 1 key.
*   **26%** buckets contain more than 1 keys, which means, collision occurs.

Following chart created by program simulation shows distribution of 20 keys
over 20 buckets.

![](/img/hash/dist-1-with-label.png)

<!--more-->


### Load Factor and Key Distribution

Let `load factor` $$ \alpha $$ to be: $$ \alpha = \frac{n}{b} $$.
`load factor` defines almost everything of a hash table.


### Load Factor `<0.75`

Normally in-memory hash table implementation keeps `load factor` lower than
**0.75**.
This makes collision rate relatively low, thus looking up is very fast.
The lower collision rate is, the less time it takes on resolving collision,
since [linear-probing] is normally used and it is very sensitive to collision
rate.

In this case, there are about **47%** buckets empty. And nearly half of these
47% will be used again by [linear-probing].

As we can see from the first chart, when `load factor` is small, key
distribution is very uneven. What we need to know is how `load factor` affects
key distribution.

Increasing `load factor` would reduce empty buckets and increase collision
rate.  The change is monotonic but not linear, as the table and picture shows
below:

| load factor(n/b) |   0 |   1 |   >1 |
| :--         | --: | --: |  --: |
| 0.5         | 61% | 30% |   9% |
| 0.75        | 47% | 35% |  17% |
| **1.0**     | 37% | 37% |  26% |
| 2.0         | 14% | 27% |  59% |
| 5.0         | 01% | 03% |  96% |
| 10.0        | 00% | 00% | 100% |

![](/img/hash/load-factor-empty-collision.png)

> **0.75** has been chosen as upper limit of `load factor` not only because
> of concern of collision rate, but also because of the way [linear-probing]
> works. That is a little bit out of this article.


### Tips

-   It is **impossible** to use hash table with low space overload and at the
    same time, with low collision rate.
    -   Counter intuitive is that just-enough buckets wastes **37%** space.

-   Use hash table only for (in memory) small data set.

-   High level language like Java or Python has builtin hash table that keeps
    `load factor` below **0.75**.

-   Hash table does **NOT** uniformly distribute small set of keys over all
    buckets.


### Load Factor `>1.0`

When `load factor` is greater than `1.0`, [linear-probing] can not work any
more, since there are not enough buckets for all keys. [chaining] keys in a
single bucket with [linked-list] is a practical method to resolve collision.

[linked-list] works well only when `load factor` is not very large, since
[linked-list] operation has `O(n)` time complexity.
For very large `load factor` [tree] or similar data structure should be considered.


### Load Factor `>10.0`

When `load factor` gets very large, the probability that a bucket is empty
converges to 0. And the key distribution converges to the average.


### The higher `load factor` is, the more uniformly keys are distributed

Let the average number of keys in each bucket be:

$$ {avg} = \frac{n}{b} $$

`100%` means a bucket contains exactly $$ {avg} $$ keys.
Following charts show what distribution is like when `load factor` is **10**,
**100** and **1000**:

![](/img/hash/dist-10.png)
![](/img/hash/dist-100.png)
![](/img/hash/dist-1000.png)


As `load factor` gets higher, the difference between the most keys bucket and
the least keys bucket get lower.

| load factor | (most-least)/most | least |
| --:     | --:    | --:   |
| 1       | 100.0% | 0     |
| 10      | 88.0%  | 2     |
| 100     | 41.2%  | 74    |
| 1,000   | 15.5%  | 916   |
| 10,000  | 5.1%   | 9735  |
| 100,000 | 1.6%   | 99161 |


### Calculation

Most of numbers from above are from program simulation.
From this chapter we are going to learn more about distribution statistics in math.

*   `0` key: $$ b e^{-\frac{n}{b}} $$
*   `1` key: $$ n e^{ - \frac{n}{b} } $$
*   `>1` key: $$ b - b e^{-\frac{n}{b}} - n e^{ - \frac{n}{b} } $$

### Number of Empty Buckets

The chance a key **NOT** in a bucket is: $$ \frac{b-1}{b} $$.
Since: $$ \lim_{b\to \infty} (1+\frac{1}{b})^b = e $$.
the probability of a bucket being empty is:

$$
(\frac{b-1}{b})^n = ((1- \frac{1}b)^b)^{\frac{n}{b}} = e^{-\frac{n}{b}}
$$

Thus the number of empty buckets is:

$$ b e^{-\frac{n}{b}} $$

### Number of Buckets Having 1 Key

The probability of a bucket having exactly 1 key is:

$$
{n \choose 1} ( 1 - \frac{1}{b} )^{n-1} ( \frac{1}{b} )^1 = \frac{n}{b} e^{-\frac{n}{b}}
$$

> One of the `n` keys is in this bucket, and at the same time, no other key
> is in this bucket:

The number of buckets having exactly 1 key is:

$$ b\frac{n}{b} e^{-\frac{n}{b}} = n e^{ - \frac{n}{b} } $$


### Number of Buckets Having More Than One Key

$$ b - b e^{-\frac{n}{b}} - n e^{ - \frac{n}{b} } $$


### Distribution Uniformity

Similarly, probability of a bucket having exactly `x` keys is:

$$
p(i) = {n \choose x} ( \frac{1}{b} )^{ i } ( 1 - \frac{1}{b} )^{n-i}
$$

The probability distribution is [binomial-distribution].

And we want to know how many keys there are in the bucket that has least keys
and the bucket that has most keys.


### Approximation by Normal Distribution

When `n` and `b` is large, binomial distribution can be approximated by
[normal-distribution] for uniformity estimation.

Let $$ p = \frac{1}{b} $$. The probability of a bucket that has exactly `x`
keys is:

$$
p(i) = {n \choose i}p^i(1-p)^{n-i}
\approx \frac{1}
             {\sigma \sqrt{2 \pi} }
        e^{ - \frac{(i-\mu)^2}{2 \sigma^2} }
$$

Where:

$$
\mu = np \\
\sigma^2 = np(1-p) \\
$$

The probability that a bucket has **less** than `x` keys is:

$$
P(x) = \sum_{i=0}^x p(i)
$$

Thus in this hash table, the total number of buckets those have less than `x` keys is:

$$
b \cdot P(x) = b \cdot \sum_{i=0}^x p(i)
$$

Choose `x` so that the total number of such buckets is `1`. Then this only
bucket must be the one that has least keys. So find `x` that satisfies:

$$
b \cdot \sum_{i=0}^x p(i) = 1
$$

With this `x`, the expected number of keys in this bucket is:

$$
N_{min} =
\frac{ \sum_{i=0}^x i \cdot p(i) }
     { \sum_{i=0}^x p(i) }
= b \cdot \sum_{i=0}^x i \cdot p(i)
\approx b \int_{i=0}^x i \cdot p(i) di
$$

Since normal distribution is symmetric:

$$
N_{max} + N_{min} = 2 \mu = 2 \frac{n}{b}
$$

### Find `x`

Now what we need to do is to find `x` in order to find
$$ N_{max} $$ and $$ \ N_{min} $$.

Probability of a bucket that contains less than `x` keys is:

$$
\sum_{i=0}^x p(i)
\approx \int_{0}^{x} p(i) di
\approx \int_{-\infty}^{x} p(i) di
= \Phi( \frac{x-\mu}\sigma )
$$

$$ \Phi(x) $$
is [cdf] of standard normal distribution. When `x - u` is close to `0`, it is
approximated by:

$$
\Phi(x)\; =\;0.5+\frac{1}{\sqrt{2\pi}}\cdot e^{-x^2/2}\left[x+\frac{x^3}{3}+\frac{x^5}{3\cdot 5}+\cdots+\frac{x^{2n+1}}{(2n+1)!!} + \cdots\right]
$$

By iterating `x` backward from `u` to `0`, we can find the solution to

$$ b \cdot \Phi(\frac{x-\mu}\sigma) = 1 $$

Then use this `x` we can find $$ N_{min} $$ and $$ N_{max} $$.

### Simulations in Python

Several simulation programs used in this post is here:
[hash-simulation](https://gist.github.com/drmingdrmer/f94b945cf7d5f287eb78)


### Reference

*   [linear-probing]
*   [double-hash]
*   [normal-distribution]
*   [binomial-distribution]
*   [cdf]

[cdf]: http://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function
[normal-distribution]: http://en.wikipedia.org/wiki/Normal_distribution
[binomial-distribution]: http://en.wikipedia.org/wiki/Binomial_distribution
[linear-probing]: http://en.wikipedia.org/wiki/Linear_probing
[tree]: http://en.wikipedia.org/wiki/Tree_(ata_structure)
[linked-list]: http://en.wikipedia.org/wiki/Linked_list
[double-hash]: http://en.wikipedia.org/wiki/Double_hashing
[chaining]: http://en.wikipedia.org/wiki/Hash_table#Separate_chaining
[sparse-hash]: http://code.google.com/p/sparsehash/
