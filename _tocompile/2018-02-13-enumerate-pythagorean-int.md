---
layout:     post
title:      "枚举所有整勾股数"
date:       2018 Feb 13
categories: math
tags:       math pythagorean 勾股数
---

<!-- mdtoc start -->

- [首先枚举所有互质的整勾股数]({{page.url}}#首先枚举所有互质的整勾股数)
    - [一组互质的x, y对应一组互质的整勾股数a, b, c]({{page.url}}#一组互质的x-y对应一组互质的整勾股数a-b-c)
    - [一组互质的整勾股数a, b, c对应一组互质的x, y]({{page.url}}#一组互质的整勾股数a-b-c对应一组互质的x-y)
        - [现在证明如果a, b, c是整勾股数且互质, x, y 一定是整数]({{page.url}}#现在证明如果a-b-c是整勾股数且互质-x-y-一定是整数)
- [然后在通过对x, y乘以一个整倍数来枚举出所有的整勾股数.]({{page.url}}#然后在通过对x-y乘以一个整倍数来枚举出所有的整勾股数)


<!-- mdtoc end   -->

<a class="md-anchor" name="首先枚举所有互质的整勾股数"></a>

# 首先枚举所有互质的整勾股数

假设a, b, c 是一组整勾股数 且互质.

> a, b, c中任意2个互质可以确定3个数都互质: $ (ua)^2 + (ub)^2 = (uc)^2 $



<a class="md-anchor" name="一组互质的x-y对应一组互质的整勾股数a-b-c"></a>

## 一组互质的x, y对应一组互质的整勾股数a, b, c

<!--excerpt-->

勾股数可以写成 $ x^2 - y^2, 2xy, x^2 + y^2 $ 的形式, 因为
$ (x^2 - y^2)^2 + (2xy)^2 = (x^2 + y^2)^2 $

**结论1: 如果x, y是互质整数, 则一组 x, y 对应一组互质整勾股数 a, b, c**.

<!--more-->

<a class="md-anchor" name="一组互质的整勾股数a-b-c对应一组互质的x-y"></a>

## 一组互质的整勾股数a, b, c对应一组互质的x, y

勾股数现在可以表示成:

$ a = x^2 - y^2 $

$ b = 2xy $

$ c = x^2 + y^2 $

从上面可以解得通过a, b, c表示x, y的形式:

$ x^2 = \frac{c+a}{2} $

$ y^2 = \frac{c-a}{2} $

$ 2xy = b $


<a class="md-anchor" name="现在证明如果a-b-c是整勾股数且互质-x-y-一定是整数"></a>

### 现在证明如果a, b, c是整勾股数且互质, x, y 一定是整数


因为a, c互质, 所以 $ x^2, y^2 $互质.

将$ x^2, y^2 $写成质因子相乘的形式, x, y没有公共因子:

$ x^2 = p_1^{q_1} p_2^{q_2} ... p_n^{q_n} $

$ y^2 = p_{n+1}^{q_{n+1}} p_{n+2}^{q_{n+2}} ... p_m^{q_m} $

而且我们知道
$ 2xy = p_1^{0.5q_1} p_2^{0.5q_2} ... p_m^{0.5q_m} = b $
是整数.
所以 $ q_i $ 必须都是偶数, 否则$ 2xy = b $不是整数.

所以x, y都是整数.

**结论2: 一组互质的勾股数a, b, c对应一组互质的x, y**

由结论1 和 结论2知道: 互质的x, y和互质的整勾股数是一一对应的.


<a class="md-anchor" name="然后在通过对x-y乘以一个整倍数来枚举出所有的整勾股数"></a>

# 然后在通过对x, y乘以一个整倍数来枚举出所有的整勾股数.
