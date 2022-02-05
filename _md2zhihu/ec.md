
<!-- mdtoc start -->

-   [内容简介](%7B%7Bpage.url%7D%7D#%E5%86%85%E5%AE%B9%E7%AE%80%E4%BB%8B)
-   [分布式系统的可靠性问题: 冗余和多副本](%7B%7Bpage.url%7D%7D#%E5%88%86%E5%B8%83%E5%BC%8F%E7%B3%BB%E7%BB%9F%E7%9A%84%E5%8F%AF%E9%9D%A0%E6%80%A7%E9%97%AE%E9%A2%98-%E5%86%97%E4%BD%99%E5%92%8C%E5%A4%9A%E5%89%AF%E6%9C%AC)
-   [EC的基本原理](%7B%7Bpage.url%7D%7D#ec%E7%9A%84%E5%9F%BA%E6%9C%AC%E5%8E%9F%E7%90%86)
    -   [栗子🌰1: 实现k+1的冗余策略, 大概需要小学3年级的数学知识](%7B%7Bpage.url%7D%7D#%E6%A0%97%E5%AD%901-%E5%AE%9E%E7%8E%B0k1%E7%9A%84%E5%86%97%E4%BD%99%E7%AD%96%E7%95%A5-%E5%A4%A7%E6%A6%82%E9%9C%80%E8%A6%81%E5%B0%8F%E5%AD%A63%E5%B9%B4%E7%BA%A7%E7%9A%84%E6%95%B0%E5%AD%A6%E7%9F%A5%E8%AF%86)
    -   [栗子🌰2: 实现k+m的冗余策略, 大概需要初中2年级的数学知识](%7B%7Bpage.url%7D%7D#%E6%A0%97%E5%AD%902-%E5%AE%9E%E7%8E%B0km%E7%9A%84%E5%86%97%E4%BD%99%E7%AD%96%E7%95%A5-%E5%A4%A7%E6%A6%82%E9%9C%80%E8%A6%81%E5%88%9D%E4%B8%AD2%E5%B9%B4%E7%BA%A7%E7%9A%84%E6%95%B0%E5%AD%A6%E7%9F%A5%E8%AF%86)
        -   [增加1个校验块, 变成k+2](%7B%7Bpage.url%7D%7D#%E5%A2%9E%E5%8A%A01%E4%B8%AA%E6%A0%A1%E9%AA%8C%E5%9D%97-%E5%8F%98%E6%88%90k2)
        -   [实现k+m 的冗余](%7B%7Bpage.url%7D%7D#%E5%AE%9E%E7%8E%B0km-%E7%9A%84%E5%86%97%E4%BD%99)

-   [EC编码矩阵的几何解释](%7B%7Bpage.url%7D%7D#ec%E7%BC%96%E7%A0%81%E7%9F%A9%E9%98%B5%E7%9A%84%E5%87%A0%E4%BD%95%E8%A7%A3%E9%87%8A)
    -   [k=2, 为2个数据块生成冗余校验块](%7B%7Bpage.url%7D%7D#k2-%E4%B8%BA2%E4%B8%AA%E6%95%B0%E6%8D%AE%E5%9D%97%E7%94%9F%E6%88%90%E5%86%97%E4%BD%99%E6%A0%A1%E9%AA%8C%E5%9D%97)
    -   [k=3, 4, 5...时的数据块的冗余](%7B%7Bpage.url%7D%7D#k3-4-5%E6%97%B6%E7%9A%84%E6%95%B0%E6%8D%AE%E5%9D%97%E7%9A%84%E5%86%97%E4%BD%99)
        -   [通过高次曲线生成冗余数据](%7B%7Bpage.url%7D%7D#%E9%80%9A%E8%BF%87%E9%AB%98%E6%AC%A1%E6%9B%B2%E7%BA%BF%E7%94%9F%E6%88%90%E5%86%97%E4%BD%99%E6%95%B0%E6%8D%AE)
        -   [从曲线方程得到的系数矩阵](%7B%7Bpage.url%7D%7D#%E4%BB%8E%E6%9B%B2%E7%BA%BF%E6%96%B9%E7%A8%8B%E5%BE%97%E5%88%B0%E7%9A%84%E7%B3%BB%E6%95%B0%E7%9F%A9%E9%98%B5)

-   [EC解码过程: 求解n元一次方程组](%7B%7Bpage.url%7D%7D#ec%E8%A7%A3%E7%A0%81%E8%BF%87%E7%A8%8B-%E6%B1%82%E8%A7%A3n%E5%85%83%E4%B8%80%E6%AC%A1%E6%96%B9%E7%A8%8B%E7%BB%84)
    -   [[Vandermonde] 矩阵保证方程组有解](%7B%7Bpage.url%7D%7D#vandermonde-%E7%9F%A9%E9%98%B5%E4%BF%9D%E8%AF%81%E6%96%B9%E7%A8%8B%E7%BB%84%E6%9C%89%E8%A7%A3)

-   [新世界: 伽罗华域 [Galois-Field] GF(7)](%7B%7Bpage.url%7D%7D#%E6%96%B0%E4%B8%96%E7%95%8C-%E4%BC%BD%E7%BD%97%E5%8D%8E%E5%9F%9F-galois-field-gf7)
    -   [EC在计算机里的实现: 基于 伽罗华域 [Galois-Field]](%7B%7Bpage.url%7D%7D#ec%E5%9C%A8%E8%AE%A1%E7%AE%97%E6%9C%BA%E9%87%8C%E7%9A%84%E5%AE%9E%E7%8E%B0-%E5%9F%BA%E4%BA%8E-%E4%BC%BD%E7%BD%97%E5%8D%8E%E5%9F%9F-galois-field)
    -   [栗子🌰3: 只有7个数字的新世界: GF(7)](%7B%7Bpage.url%7D%7D#%E6%A0%97%E5%AD%903-%E5%8F%AA%E6%9C%897%E4%B8%AA%E6%95%B0%E5%AD%97%E7%9A%84%E6%96%B0%E4%B8%96%E7%95%8C-gf7)
        -   [模7新世界中的 **加法**](%7B%7Bpage.url%7D%7D#%E6%A8%A17%E6%96%B0%E4%B8%96%E7%95%8C%E4%B8%AD%E7%9A%84-%E5%8A%A0%E6%B3%95)
        -   [模7新世界中的 **减法**](%7B%7Bpage.url%7D%7D#%E6%A8%A17%E6%96%B0%E4%B8%96%E7%95%8C%E4%B8%AD%E7%9A%84-%E5%87%8F%E6%B3%95)
        -   [模7新世界中的 **乘法** 和 **除法**](%7B%7Bpage.url%7D%7D#%E6%A8%A17%E6%96%B0%E4%B8%96%E7%95%8C%E4%B8%AD%E7%9A%84-%E4%B9%98%E6%B3%95-%E5%92%8C-%E9%99%A4%E6%B3%95)

    -   [栗子🌰4: 模7新世界直线方程-1](%7B%7Bpage.url%7D%7D#%E6%A0%97%E5%AD%904-%E6%A8%A17%E6%96%B0%E4%B8%96%E7%95%8C%E7%9B%B4%E7%BA%BF%E6%96%B9%E7%A8%8B-1)
    -   [栗子🌰5: 模7新世界直线方程-2](%7B%7Bpage.url%7D%7D#%E6%A0%97%E5%AD%905-%E6%A8%A17%E6%96%B0%E4%B8%96%E7%95%8C%E7%9B%B4%E7%BA%BF%E6%96%B9%E7%A8%8B-2)
    -   [栗子🌰6: 模7新世界中的二次曲线方程](%7B%7Bpage.url%7D%7D#%E6%A0%97%E5%AD%906-%E6%A8%A17%E6%96%B0%E4%B8%96%E7%95%8C%E4%B8%AD%E7%9A%84%E4%BA%8C%E6%AC%A1%E6%9B%B2%E7%BA%BF%E6%96%B9%E7%A8%8B)
    -   [模7新世界里的EC](%7B%7Bpage.url%7D%7D#%E6%A8%A17%E6%96%B0%E4%B8%96%E7%95%8C%E9%87%8C%E7%9A%84ec)

-   [EC使用的新世界 [Galois-Field] GF(256)](%7B%7Bpage.url%7D%7D#ec%E4%BD%BF%E7%94%A8%E7%9A%84%E6%96%B0%E4%B8%96%E7%95%8C-galois-field-gf256)
    -   [模2的新世界: [Galois-Field] GF(2)](%7B%7Bpage.url%7D%7D#%E6%A8%A12%E7%9A%84%E6%96%B0%E4%B8%96%E7%95%8C-galois-field-gf2)
    -   [域的扩张 [Field-Extension]](%7B%7Bpage.url%7D%7D#%E5%9F%9F%E7%9A%84%E6%89%A9%E5%BC%A0-field-extension)
        -   [栗子🌰7: 实数到虚数的扩张](%7B%7Bpage.url%7D%7D#%E6%A0%97%E5%AD%907-%E5%AE%9E%E6%95%B0%E5%88%B0%E8%99%9A%E6%95%B0%E7%9A%84%E6%89%A9%E5%BC%A0)

    -   [从2到256: 扩张 GF(2)](%7B%7Bpage.url%7D%7D#%E4%BB%8E2%E5%88%B0256-%E6%89%A9%E5%BC%A0-gf2)
        -   [栗子🌰8: GF(2) 下的质多项式](%7B%7Bpage.url%7D%7D#%E6%A0%97%E5%AD%908-gf2-%E4%B8%8B%E7%9A%84%E8%B4%A8%E5%A4%9A%E9%A1%B9%E5%BC%8F)
        -   [GF(2) 扩张成 GF(2^8)](%7B%7Bpage.url%7D%7D#gf2-%E6%89%A9%E5%BC%A0%E6%88%90-gf28)

-   [实现](%7B%7Bpage.url%7D%7D#%E5%AE%9E%E7%8E%B0)
    -   [标准EC的实现](%7B%7Bpage.url%7D%7D#%E6%A0%87%E5%87%86ec%E7%9A%84%E5%AE%9E%E7%8E%B0)
        -   [EC编码: 校验数据生成](%7B%7Bpage.url%7D%7D#ec%E7%BC%96%E7%A0%81-%E6%A0%A1%E9%AA%8C%E6%95%B0%E6%8D%AE%E7%94%9F%E6%88%90)
        -   [EC解码](%7B%7Bpage.url%7D%7D#ec%E8%A7%A3%E7%A0%81)
        -   [Vandermonde 矩阵的可逆性](%7B%7Bpage.url%7D%7D#vandermonde-%E7%9F%A9%E9%98%B5%E7%9A%84%E5%8F%AF%E9%80%86%E6%80%A7)
        -   [GF256 下的 Vandermonde 矩阵的可逆性](%7B%7Bpage.url%7D%7D#gf256-%E4%B8%8B%E7%9A%84-vandermonde-%E7%9F%A9%E9%98%B5%E7%9A%84%E5%8F%AF%E9%80%86%E6%80%A7)

    -   [数据恢复IO优化: LRC: [Local-Reconstruction-Code]](%7B%7Bpage.url%7D%7D#%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8Dio%E4%BC%98%E5%8C%96-lrc-local-reconstruction-code)
        -   [LRC 的校验块生成](%7B%7Bpage.url%7D%7D#lrc-%E7%9A%84%E6%A0%A1%E9%AA%8C%E5%9D%97%E7%94%9F%E6%88%90)
        -   [LRC 的数据恢复](%7B%7Bpage.url%7D%7D#lrc-%E7%9A%84%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D)

    -   [工程优化](%7B%7Bpage.url%7D%7D#%E5%B7%A5%E7%A8%8B%E4%BC%98%E5%8C%96)

-   [分析](%7B%7Bpage.url%7D%7D#%E5%88%86%E6%9E%90)
    -   [可靠性分析](%7B%7Bpage.url%7D%7D#%E5%8F%AF%E9%9D%A0%E6%80%A7%E5%88%86%E6%9E%90)
    -   [IO消耗](%7B%7Bpage.url%7D%7D#io%E6%B6%88%E8%80%97)

-   [参考](%7B%7Bpage.url%7D%7D#%E5%8F%82%E8%80%83)

<!-- mdtoc end   -->

<!--excerpt-->

<a class="md-anchor" name="内容简介"></a>

# 内容简介

[Erasure-Code](https://en.wikipedia.org/wiki/Erasure_code), 简称 EC, 也叫做 **擦除码** 或 **纠删码**,
指使用 范德蒙([Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix)) 矩阵的 里德-所罗门码([Reed-Solomon](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction)) 擦除码算法.

**EC 本身是1组数据冗余和恢复的算法的统称**.

本文以 [Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix) 矩阵的 [Reed-Solomon](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction) 来解释 EC 的原理.

术语定义:

-   <img src="https://www.zhihu.com/equation?tex=d_j" alt="d_j" class="ee_img tr_noresize" eeimg="1"> 表示数据块.
-   <img src="https://www.zhihu.com/equation?tex=y_i" alt="y_i" class="ee_img tr_noresize" eeimg="1"> 表示通过数据块计算得来的, 作为数据冗余的校验块.
-   <img src="https://www.zhihu.com/equation?tex=u_j" alt="u_j" class="ee_img tr_noresize" eeimg="1"> 表示丢失的, 需要恢复的数据块.
-   k 表示数据块的数量.
-   m 表示校验块的数量.

<!--more-->

本文内容包括:

-   第1节 [分布式系统的可靠性问题: 冗余和多副本](%7B%7Bpage.url%7D%7D#ec-ncopy)
    提出EC需要解决的问题.

-   希望对分布式存储领域增加了解的同学,
    可以只阅读 [EC的基本原理](%7B%7Bpage.url%7D%7D#ec-basic) 部分.

    这部分会用到1些中学的数学知识,
    逐步用举栗子🌰的方式给出了EC算法的直观解释.

    它和真正实现层面的EC原理是一致的, 但不深入到太多数学层面的内容.

-   已经对EC工作方式有些了解, 希望更深入了解其数学原理的读者, 可以直接从
    [EC编码矩阵的几何解释](%7B%7Bpage.url%7D%7D#ec-matrix) 开始阅读.

    这部分解释了EC的编码矩阵的原理和含义,
    但不包括更底层数学的讨论.

    [伽罗华域GF(7)](%7B%7Bpage.url%7D%7D#ec-gf7) 和 [伽罗华域GF(256)](%7B%7Bpage.url%7D%7D#ec-gf256) 开始介绍如何将EC应用到计算机上的方法,
    从这部分开始EC会用到1些抽象代数中的知识.

-   需要动手扣腚解决分布式存储问题的猿, 如果对数学原理不感兴趣,
    但对工程实践方面有兴趣的话, 可以参考 [实现](%7B%7Bpage.url%7D%7D#ec-impl).

-   需要对存储策略规划的架构师, 可以直接参考数值分析部分 [分析](%7B%7Bpage.url%7D%7D#ec-analysis).

<a name="ec-ncopy"></a>

<a class="md-anchor" name="分布式系统的可靠性问题-冗余和多副本"></a>

# 分布式系统的可靠性问题: 冗余和多副本

在分布式系统中, 第1个要解决的问题是可靠性问题,
因为服务器会宕机,磁盘会掉,光纤会被挖掘机铲断, 机房会被大雨淹没.
数据存储多份才可以达到工业可用的可靠性.

**一般还必须让数据的多个副本分布在不同的服务器, 机架或机房里才能真正达到高可靠**.

数据可靠了之后才需要讨论数据的一致性和性能等问题.
(也可能, 一致性和可靠性是并列第一的😄).

提高可靠性也很直接, 一般的解决方式就是 **对一份数据存储多个副本**.

> 副本数一般选择3: <br/>
>   3副本结合当前经验上的磁盘的损坏率(大约是年损坏率7%),
>   大约可以达到一个工业可接受的可靠性,
>   这个可靠性的预期大约是11个9以上(99.999999999%的概率不丢数据).


下图摘自 [backblaze发布的硬盘故障率统计](https://www.backblaze.com/blog/hard-drive-reliability-stats-q1-2016/)

![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec/1fdaccd1a69c0ddc-drive-stats-2016-q1-failure-by-mfg.jpg)

如果我有2块数据(每块可能是1个1G大小的电影): <img src="https://www.zhihu.com/equation?tex=%20d_1%20" alt=" d_1 " class="ee_img tr_noresize" eeimg="1"> 和 <img src="https://www.zhihu.com/equation?tex=%20d_2%20" alt=" d_2 " class="ee_img tr_noresize" eeimg="1">,
为了达到高可靠性, 我需要对每个数据复制3份,
并放在不同的服务器上以保证足够分散,
数据在服务器上的保存的位置大概是酱:

<img src="https://www.zhihu.com/equation?tex=%28d_1%2C%20d_1%2C%20d_1%29%2C%20%5C%5C%28d_2%2C%20d_2%2C%20d_2%29%2C%20%5C%5C...%5C%5C" alt="(d_1, d_1, d_1), \\(d_2, d_2, d_2), \\...\\" class="ee_img tr_noresize" eeimg="1">

第1列的<img src="https://www.zhihu.com/equation?tex=d_1%2C%20d_2" alt="d_1, d_2" class="ee_img tr_noresize" eeimg="1">在第1个服务器上,<br/>
第2列的<img src="https://www.zhihu.com/equation?tex=d_1%2C%20d_2" alt="d_1, d_2" class="ee_img tr_noresize" eeimg="1">在第2个服务器上,<br/>
第3列的<img src="https://www.zhihu.com/equation?tex=d_1%2C%20d_2" alt="d_1, d_2" class="ee_img tr_noresize" eeimg="1">在第3个服务器上.

> 这种3副本的策略下, 总的存储冗余度是 300% <br/>
> 空间浪费是200%


当然有些时候为了降低成本, 只存储2个副本, 这时冗余度是200%, 也浪费了1倍的空间:

<img src="https://www.zhihu.com/equation?tex=%28d_1%2C%20d_1%29%2C%20%5C%5C%28d_2%2C%20d_2%29%2C%20%5C%5C...%5C%5C" alt="(d_1, d_1), \\(d_2, d_2), \\...\\" class="ee_img tr_noresize" eeimg="1">

那么, 能否用较少的冗余, 来实现同样较高的可靠性,
就成了分布式存储的一个重要研发的方向.

这就是本文介绍的 EC 需要解决的问题.
接下来, 我们通过几个例子, 1步步介绍 EC 的原理和实现机制.

<a name="ec-basic"></a>

<a class="md-anchor" name="ec的基本原理"></a>

# EC的基本原理

<a class="md-anchor" name="栗子1-实现k1的冗余策略-大概需要小学3年级的数学知识"></a>

## 栗子🌰1: 实现k+1的冗余策略, 大概需要小学3年级的数学知识

> Q: 有3个自然数, 能否做到再记录第4个数字,
> 让任何一个数字丢失的时候都可以将其找回?


这个问题很简单, 记录这3个数字的和:
假设3个数字是: <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%2C%20d_3%20" alt=" d_1, d_2, d_3 " class="ee_img tr_noresize" eeimg="1">;
再存储一个数: <img src="https://www.zhihu.com/equation?tex=%20y_1%20%3D%20d_1%20%2B%20d_2%20%2B%20d_3%20" alt=" y_1 = d_1 + d_2 + d_3 " class="ee_img tr_noresize" eeimg="1">.

-   存储的过程就是存储这4个数字: <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%2C%20d_3%2C%20y_1%20" alt=" d_1, d_2, d_3, y_1 " class="ee_img tr_noresize" eeimg="1">:

-   数据丢失后要找回时:

    -   这样如果 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%2C%20d_3%20" alt=" d_1, d_2, d_3 " class="ee_img tr_noresize" eeimg="1"> 任意一个丢失, 例如 <img src="https://www.zhihu.com/equation?tex=%20d_1%20" alt=" d_1 " class="ee_img tr_noresize" eeimg="1"> 丢失了,
        我们都可以通过 <img src="https://www.zhihu.com/equation?tex=%20d_1%20%3D%20y_1%20-%20d_2%20-%20d_3%20" alt=" d_1 = y_1 - d_2 - d_3 " class="ee_img tr_noresize" eeimg="1"> 来得到 <img src="https://www.zhihu.com/equation?tex=%20d_1%20" alt=" d_1 " class="ee_img tr_noresize" eeimg="1">.

    -   如果 <img src="https://www.zhihu.com/equation?tex=%20y_1%20" alt=" y_1 " class="ee_img tr_noresize" eeimg="1"> 丢失, 则再次取 <img src="https://www.zhihu.com/equation?tex=%20d_1%20%2B%20d_2%20%2B%20d_3%20" alt=" d_1 + d_2 + d_3 " class="ee_img tr_noresize" eeimg="1"> 的和就可以将 <img src="https://www.zhihu.com/equation?tex=%20y_1%20" alt=" y_1 " class="ee_img tr_noresize" eeimg="1"> 找回.

在上面这个简单的系统中, 总共存储了4份数据, 有效的数据是3份. <br/>
冗余是133%,
它的可靠性和2副本的存储策略差不多: 最多允许丢失1份数据.

看起来这是一个不错的解决方案:<br/>
我们用**133%**的冗余,
实现了和2副本的 **200%** 冗余 **差不多**的可靠性! 如下:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tr class="header">
<th style="text-align: left;">策略</th>
<th style="text-align: left;">冗余度</th>
<th style="text-align: left;">可靠性</th>
<th style="text-align: left;">存储策略示意</th>
</tr>
<tr class="odd">
<td style="text-align: left;">2副本</td>
<td style="text-align: left;">200%</td>
<td style="text-align: left;">允许丢1块: <br /><span class="math display">1 × 10<sup> − 8</sup></span><br /></td>
<td style="text-align: left;"><br /><span class="math display">(<em>d</em><sub>1</sub>, <em>d</em><sub>1</sub>)</span><br />, <br /><span class="math display">(<em>d</em><sub>2</sub>, <em>d</em><sub>2</sub>)</span><br />, <br /><span class="math display">(<em>d</em><sub>3</sub>, <em>d</em><sub>3</sub>)...</span><br /></td>
</tr>
<tr class="even">
<td style="text-align: left;">3+1求和冗余</td>
<td style="text-align: left;">133%</td>
<td style="text-align: left;">允许丢1块: <br /><span class="math display">6 × 10<sup> − 8</sup></span><br /></td>
<td style="text-align: left;"><br /><span class="math display">(<em>d</em><sub>1</sub>, <em>d</em><sub>2</sub>, <em>d</em><sub>3</sub>, <em>y</em><sub>1</sub>)</span><br />, <br /><span class="math display">(<em>d</em><sub>4</sub>, <em>d</em><sub>5</sub>, <em>d</em><sub>6</sub>, <em>y</em><sub>2</sub>)...</span><br /></td>
</tr>
</table>

> 这里只是**差不多**, 还并不是完全一样,
> 后面[分析](%7B%7Bpage.url%7D%7D#ec-analysis) 1节会详细讨论可靠性的计算.<br/>
> 在讨论可靠性的时候, 一般数据丢失风险没有量级的差异, 就可以认为是比较接近的.


> 上面这个例子是和我们平时使用的 [RAID-5](https://zh.wikipedia.org/wiki/RAID#RAID_5) 基本是一样的.
> [RAID-5](https://zh.wikipedia.org/wiki/RAID#RAID_5) 通过对k个(可能是11个左右)数据块求出1份**校验和**的数据块.
> 存储这份校验块, 并允许1块(数据或校验)丢失后可以找回.
> 
> 当然在工程上, [RAID-5](https://zh.wikipedia.org/wiki/RAID#RAID_5) 的计算和自然数的求和还有些差异. 后面继续撩.


以上的这种**求和冗余**策略, 就是 EC 的核心思路.

---

如果你对存储感兴趣但不希望太多深入细节,
到这里差不多已经比较直观地了解 EC 的原理了.

如果你还有浓厚的兴趣继续读下去,好极!

接下来将上面的内容做些扩展,
后面章节会继续深入1点点, 逐步把上面提到的**求和冗余**
推广成1个生产环境可用的存储策略,
同时也会逐步引入更多的数学来完善这个策略.

<a class="md-anchor" name="栗子2-实现km的冗余策略-大概需要初中2年级的数学知识"></a>

## 栗子🌰2: 实现k+m的冗余策略, 大概需要初中2年级的数学知识

现在我们在k+1的冗余策略基础上, 增加更多的校验块, 来实现任意k+m的冗余策略.

<a class="md-anchor" name="增加1个校验块-变成k2"></a>

### 增加1个校验块, 变成k+2

现在让我们把问题再推进1步.
上面我们通过多增加1份的冗余, 实现了和2副本差不多的可靠性(允许丢失1块数据).
那么我们如果要实现和3副本差不多的可靠性呢(允许丢失2块数据)?

> Q: 有3块数据: <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%2C%20d_3%20" alt=" d_1, d_2, d_3 " class="ee_img tr_noresize" eeimg="1"> <br/>
> 可否另外再存储2个冗余的校验块(共5块), 让整个系统任意丢失2份数据时都能找回?


在**k+1求和**的策略里, 我们实际上是给所有的数据块和校验块建立了一个方程
<img src="https://www.zhihu.com/equation?tex=%20d_1%20%2B%20d_2%20%2B%20d_3%20%3D%20y_1%20" alt=" d_1 + d_2 + d_3 = y_1 " class="ee_img tr_noresize" eeimg="1">,
来描述他们整体的关系.

现在, 如果要增加可丢失的数据块数, 简单的把 <img src="https://www.zhihu.com/equation?tex=%20y_1%20" alt=" y_1 " class="ee_img tr_noresize" eeimg="1"> 存2次是不够的,
假设计算了2个校验块:

<img src="https://www.zhihu.com/equation?tex=d_1%20%2B%20d_2%20%2B%20d_3%20%3D%20y_1%20%5C%5Cd_1%20%2B%20d_2%20%2B%20d_3%20%3D%20y_2%20%5C%5C%28y_1%20%3D%20y_2%29%5C%5C" alt="d_1 + d_2 + d_3 = y_1 \\d_1 + d_2 + d_3 = y_2 \\(y_1 = y_2)\\" class="ee_img tr_noresize" eeimg="1">

-   存储的过程定义为: 存储 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%2C%20d_3%2C%20y_1%2C%20y_2%20" alt=" d_1, d_2, d_3, y_1, y_2 " class="ee_img tr_noresize" eeimg="1"> 这5个数字.

-   需要恢复数据时:
    如果 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%20" alt=" d_1, d_2 " class="ee_img tr_noresize" eeimg="1"> 都丢失了(<img src="https://www.zhihu.com/equation?tex=%20u_1%2C%20u_2%20" alt=" u_1, u_2 " class="ee_img tr_noresize" eeimg="1"> 表示),
    下面这个关于<img src="https://www.zhihu.com/equation?tex=%20u_1%2C%20u_2%20" alt=" u_1, u_2 " class="ee_img tr_noresize" eeimg="1">的线性方程是有无穷多解的:

    <img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bcases%7Du_1%20%2B%20u_2%20%2B%20d_3%20%3D%20y_1%20%5C%5Cu_1%20%2B%20u_2%20%2B%20d_3%20%3D%20y_2%5Cend%7Bcases%7D%5C%5C" alt="\begin{cases}u_1 + u_2 + d_3 = y_1 \\u_1 + u_2 + d_3 = y_2\end{cases}\\" class="ee_img tr_noresize" eeimg="1">

    我们没有办法从这个方程组里解出 <img src="https://www.zhihu.com/equation?tex=%20u_1%2C%20u_2%20" alt=" u_1, u_2 " class="ee_img tr_noresize" eeimg="1"> 的值, 因为这2个方程是一样的,
    没有提供更多的信息.

> 所以我们现在需要做的是, 设计一个计算第2个校验块 <img src="https://www.zhihu.com/equation?tex=%20y_2%20" alt=" y_2 " class="ee_img tr_noresize" eeimg="1"> 的方法:<br/>
> **使得当 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%20" alt=" d_1, d_2 " class="ee_img tr_noresize" eeimg="1">丢失时方程组有解**.


一个简单直接的思路是, 计算<img src="https://www.zhihu.com/equation?tex=%20y_2%20" alt=" y_2 " class="ee_img tr_noresize" eeimg="1"> 时, 给每个数据 <img src="https://www.zhihu.com/equation?tex=%20d_j%20" alt=" d_j " class="ee_img tr_noresize" eeimg="1"> 增加1个不同的系数:

-   计算<img src="https://www.zhihu.com/equation?tex=y_1" alt="y_1" class="ee_img tr_noresize" eeimg="1">时, 对每个数字乘以1, 1, 1, 1 ...
-   计算<img src="https://www.zhihu.com/equation?tex=y_2" alt="y_2" class="ee_img tr_noresize" eeimg="1">时, 对每个数字乘以1, 2, 4, 8 ...

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Baligned%7Dd_1%20%2B%20d_2%20%2B%20d_3%20%20%20%20%20%26%20%3D%20y_1%20%5C%5Cd_1%20%2B%202%20d_2%20%2B%204%20d_3%20%26%20%3D%20y_2%5Cend%7Baligned%7D%5C%5C" alt="\begin{aligned}d_1 + d_2 + d_3     & = y_1 \\d_1 + 2 d_2 + 4 d_3 & = y_2\end{aligned}\\" class="ee_img tr_noresize" eeimg="1">

-   存储的过程任然定义为:
    存储 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%2C%20d_3%2C%20y_1%2C%20y_2%20" alt=" d_1, d_2, d_3, y_1, y_2 " class="ee_img tr_noresize" eeimg="1"> 这5个数字.

-   数据恢复的时候,
    如果 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%20" alt=" d_1, d_2 " class="ee_img tr_noresize" eeimg="1"> 丢失, 同样用 <img src="https://www.zhihu.com/equation?tex=%20u_1%2C%20u_2%20" alt=" u_1, u_2 " class="ee_img tr_noresize" eeimg="1">表示,
    我们可以使用剩下的 <img src="https://www.zhihu.com/equation?tex=%20d_3%2C%20y_1%2C%20y_2%20" alt=" d_3, y_1, y_2 " class="ee_img tr_noresize" eeimg="1">
    来建里1个关于 <img src="https://www.zhihu.com/equation?tex=%20u_1%2C%20u_2%20" alt=" u_1, u_2 " class="ee_img tr_noresize" eeimg="1"> 的二元一次方程组:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bcases%7D%5Cbegin%7Baligned%7Du_1%20%2B%20u_2%20%20%20%26%20%3D%20y_1%20-%20d_3%20%5C%5Cu_1%20%2B%202%20u_2%20%26%20%3D%20y_2%20-%204%20d_3%5Cend%7Baligned%7D%5Cend%7Bcases%7D%5C%5C" alt="\begin{cases}\begin{aligned}u_1 + u_2   & = y_1 - d_3 \\u_1 + 2 u_2 & = y_2 - 4 d_3\end{aligned}\end{cases}\\" class="ee_img tr_noresize" eeimg="1">

解出上面这个方程组, 就找回了丢失的 <img src="https://www.zhihu.com/equation?tex=%20u_1%2C%20u_2%20" alt=" u_1, u_2 " class="ee_img tr_noresize" eeimg="1">.

**感谢对我们负责的初中班主任, 把体育课帮我们改成了数学习题课,
让我们还记得这个二元一次方程组好像通过消元, 就能解出 <img src="https://www.zhihu.com/equation?tex=%20u_1%2C%20u_2%20" alt=" u_1, u_2 " class="ee_img tr_noresize" eeimg="1">
的值**

`<(￣︶￣)>`

> 以上这种**加系数**计算校验块的方式, 就是[RAID-6](https://zh.wikipedia.org/wiki/RAID#RAID_6)的基本工作方式:<br/>
> [RAID-6](https://zh.wikipedia.org/wiki/RAID#RAID_6)为k个数据块之外再多存储2个校验数据,
> 当整个系统丢失2块数据时, 都可以找回.


> 为什么计算 <img src="https://www.zhihu.com/equation?tex=%20y_2%20" alt=" y_2 " class="ee_img tr_noresize" eeimg="1"> 的系数是1, 2, 4, 8...?<br/>
> 系数的选择有很多种方法, 1, 2, 4, 8是其中一个.
> 只要保证最终丢失2个数字构成的方程组有唯一解就可以.
> 这里选择1, 2, 3, 4...也可以.


到这里, 有理数下k+2的EC的算法大概就出来了,
我们可以实现k+2的冗余策略, 通过166%的冗余, 实现**差不多**和三副本300%一样的可靠性.

具体的可靠性计算参见下面的: [分析](%7B%7Bpage.url%7D%7D#ec-analysis)

<a class="md-anchor" name="实现km-的冗余"></a>

### 实现k+m 的冗余

如果要增加更多的冗余,让EC来实现相当于4副本差不多的可靠性: k+3,
我们需要给上面的策略再增加一个校验块 <img src="https://www.zhihu.com/equation?tex=%20y_3%20" alt=" y_3 " class="ee_img tr_noresize" eeimg="1">,

而 <img src="https://www.zhihu.com/equation?tex=%20y_3%20" alt=" y_3 " class="ee_img tr_noresize" eeimg="1"> 的计算我们需要再为所有的 <img src="https://www.zhihu.com/equation?tex=%20d_j%20" alt=" d_j " class="ee_img tr_noresize" eeimg="1"> 选择1组不同的系数,
例如1,3,9,27...来保证后面数据丢失时,得到的1个3元一次方程组是可解的:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bcases%7D%5Cbegin%7Baligned%7Dd_1%20%2B%20%20%20d_2%20%2B%20%20%20d_3%20%26%20%3D%20y_1%20%5C%5Cd_1%20%2B%202%20d_2%20%2B%204%20d_3%20%26%20%3D%20y_2%20%5C%5Cd_1%20%2B%203%20d_2%20%2B%209%20d_3%20%26%20%3D%20y_2%5Cend%7Baligned%7D%5Cend%7Bcases%7D%5C%5C" alt="\begin{cases}\begin{aligned}d_1 +   d_2 +   d_3 & = y_1 \\d_1 + 2 d_2 + 4 d_3 & = y_2 \\d_1 + 3 d_2 + 9 d_3 & = y_2\end{aligned}\end{cases}\\" class="ee_img tr_noresize" eeimg="1">

这样我们通过不断的增加不同的系数, 就可以得到任意的k+m的EC冗余存储策略的实现.

到此为止, 有理数下的EC算法就介绍完整了.
接下来的章节中, 我们会深入1点, 讨论下为什么要选择这样1组系数.

> 实际上,现实中使用的[RAID-5](https://zh.wikipedia.org/wiki/RAID#RAID_5)和[RAID-6](https://zh.wikipedia.org/wiki/RAID#RAID_6)都是 EC 的子集.
> EC 是更具通用性的算法. 但因为实现的成本(主要是计算的开销), [RAID-5](https://zh.wikipedia.org/wiki/RAID#RAID_5) 和
> [RAID-6](https://zh.wikipedia.org/wiki/RAID#RAID_6)在单机的可靠性实现中还是占主流地位.
> 
> 但随着存储量的不断增大, 百PB的存储已经不算是很极端场景了.
> [RAID-6](https://zh.wikipedia.org/wiki/RAID#RAID_6) 在单机环境下不算高的数据丢失风险在大数据量的场景中显示的越来越明显.
> 于是在云存储(大规模存储)领域, 能支持更多的冗余校验块的EC成为了主流.


<a name="ec-matrix"></a>

<a class="md-anchor" name="ec编码矩阵的几何解释"></a>

# EC编码矩阵的几何解释

上面大概介绍了如何选择 EC 生成校验块(编码过程)的系数,
我们隐约可以预感到它的系数选择可能有某种内涵,
下面我们来从最初的问题入手, 讨论下为什么会得出这样1组系数选择的方法.

EC 可以这样被理解: 为了恢复几块数据,
我们需要预先通过这几块数据 <img src="https://www.zhihu.com/equation?tex=%20d_j%20" alt=" d_j " class="ee_img tr_noresize" eeimg="1"> 另外计算出几个数值(校验块),
校验块和数据块构成1个整体,
这些校验块具备所有数据块的特征,
可以用于和其他几个数据配合起来找回丢失的数据块.

我们从比较简单的情况开始, 看下2个数据块计算(多个)EC校验块的方法:

<a class="md-anchor" name="k2-为2个数据块生成冗余校验块"></a>

## k=2, 为2个数据块生成冗余校验块

假设 现在我们有2个数据块 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%20" alt=" d_1, d_2 " class="ee_img tr_noresize" eeimg="1">. 要做2个校验块.

**我们使用1个直线的方程, 来实现数据的冗余备份和恢复**:

<img src="https://www.zhihu.com/equation?tex=%20y%20%3D%20d_1%20%2B%20d_2%20x%20%5C%5C" alt=" y = d_1 + d_2 x \\" class="ee_img tr_noresize" eeimg="1">

这条直线具备这样的特点:

-   **这条直线包含的所有数据块 <img src="https://www.zhihu.com/equation?tex=%20d_j%20" alt=" d_j " class="ee_img tr_noresize" eeimg="1"> 的信息**.

    任何1对 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%20" alt=" d_1, d_2 " class="ee_img tr_noresize" eeimg="1"> 的值就确定一条不同的直线.
    同样, 任意1条直线也唯一对应1对 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%20" alt=" d_1, d_2 " class="ee_img tr_noresize" eeimg="1"> 的值.

数据可靠性的问题就转化成了:

-   **我们要保存足够多的关于这条直线的信息, 能够在需要的时候找回这条直线.
    然后再提取直线方程的系数来找回最初存储的数据块 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%20" alt=" d_1, d_2 " class="ee_img tr_noresize" eeimg="1">**.

要保存足够多的信息, **最直观的方法就是记录这条直线上的几个点的坐标**.

因为2点可以确定一条直线, 只要拿到直线上2个点的坐标, 就能确定直线方程,
从而确定它的系数 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%20" alt=" d_1, d_2 " class="ee_img tr_noresize" eeimg="1">.

按照这样的思路, 我们重新用直线方程的方式描述数据冗余生成和数据恢复的过程:

-   生成冗余的校验数据的过程就是:

    在直线上取2个点, 记录点的坐标(这里我们总是取x = [1, 2, 3...]的自然数的值,
    所以只记录y的值就可以了)

    <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%2C%20%281%2C%20y_1%29%2C%20%282%2C%20y_2%29%20%5C%5C" alt=" d_1, d_2, (1, y_1), (2, y_2) \\" class="ee_img tr_noresize" eeimg="1">

-   恢复数据的过程就是: 已知过直线2点 <img src="https://www.zhihu.com/equation?tex=%20%281%2C%20y_1%29%2C%20%282%2C%20y_2%29%20" alt=" (1, y_1), (2, y_2) " class="ee_img tr_noresize" eeimg="1"> 来确定直线方程的过程.

**再次感谢初中班主任**

取 x 分别为 1和2:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bcases%7Dy_1%20%3D%20d_1%20%2B%20d_2%20%5C%5Cy_2%20%3D%20d_1%20%2B%202d_2%5Cend%7Bcases%7D%5C%5C" alt="\begin{cases}y_1 = d_1 + d_2 \\y_2 = d_1 + 2d_2\end{cases}\\" class="ee_img tr_noresize" eeimg="1">

我们得到了1组带冗余的数据: <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%2C%20y_1%2C%20y_2%20" alt=" d_1, d_2, y_1, y_2 " class="ee_img tr_noresize" eeimg="1">.
这4个数据中,任意丢失2个,都可以通过等式关系 <img src="https://www.zhihu.com/equation?tex=%20y%20%3D%20d_1%20%2B%20d_2%20%C2%B7%20x%20" alt=" y = d_1 + d_2 · x " class="ee_img tr_noresize" eeimg="1"> 来恢复.

> 丢失1个数据块时只用 <img src="https://www.zhihu.com/equation?tex=%20y_1%20" alt=" y_1 " class="ee_img tr_noresize" eeimg="1"> 的方程就够了.<br/>
> 丢失2个数据块时才需要解二元一次方程组. <br/>
> 如果 <img src="https://www.zhihu.com/equation?tex=%20y_1%20" alt=" y_1 " class="ee_img tr_noresize" eeimg="1">或 <img src="https://www.zhihu.com/equation?tex=%20y_2%20" alt=" y_2 " class="ee_img tr_noresize" eeimg="1">丢失, 则通过重新取点的方式恢复.


> 我们可以在直线上取任意多个点, 但恢复时最多也只需要2个点就够了.
> 在这个例子中我们实现了 2+m 的冗余策略.


<a class="md-anchor" name="k3-4-5时的数据块的冗余"></a>

## k=3, 4, 5...时的数据块的冗余

现在我们把它再推广到更一般的情况:
直线方程只需要2个值来确定, 但如果要用描点方式来为更多的数据块生成冗余数据,
我们需要使用高次的曲线, 来记录更多的数据.

例如:

-   **二次曲线抛物线 <img src="https://www.zhihu.com/equation?tex=%20y%20%3D%20a%20x%5E2%20%2B%20b%20x%20%2B%20c%20" alt=" y = a x^2 + b x + c " class="ee_img tr_noresize" eeimg="1"> 需要3个值来确定,
    同时也需要知道抛物线上的3个点的坐标来找回这条抛物线**.

<a class="md-anchor" name="通过高次曲线生成冗余数据"></a>

### 通过高次曲线生成冗余数据

如果有k个数据块, 我们把k个数据作为系数, 来定义1条关于x的高次曲线:

<img src="https://www.zhihu.com/equation?tex=y%20%3D%20d_1%20%2B%20d_2%20x%20%2B%20d_3%20x%5E2%20%2B%20...%20%2B%20d_k%20x%5E%7Bk-1%7D%5C%5C" alt="y = d_1 + d_2 x + d_3 x^2 + ... + d_k x^{k-1}\\" class="ee_img tr_noresize" eeimg="1">

-   生成m个冗余数据的过程就是:

    取m个不同的x的值(1, 2, 3...m), 记录这条曲线上m个不同点的坐标:

    <img src="https://www.zhihu.com/equation?tex=%20%281%2C%20y_1%29%2C%20%282%2C%20y_2%29%20...%20%28m%2C%20y_m%29%20%5C%5C" alt=" (1, y_1), (2, y_2) ... (m, y_m) \\" class="ee_img tr_noresize" eeimg="1">

    存储所有的数据块 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2...d_k%20" alt=" d_1, d_2...d_k " class="ee_img tr_noresize" eeimg="1">
    和所有的校验块 <img src="https://www.zhihu.com/equation?tex=%20y_1%2C%20y_2...y_m%20" alt=" y_1, y_2...y_m " class="ee_img tr_noresize" eeimg="1">.

-   恢复数据:

    当数据丢失时, 我们知道,
    平面直角坐标系上m个点可以唯一确定1条 m-1 次幂的关于x的曲线.
    确定了这条关于x的曲线,就找回了它的系数,也就是数据块 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%20...%20d_k%20" alt=" d_1, d_2 ... d_k " class="ee_img tr_noresize" eeimg="1">

**以上就是 EC 的算法的几何解释: 通过曲线上的点来确定曲线的过程**.

<a class="md-anchor" name="从曲线方程得到的系数矩阵"></a>

### 从曲线方程得到的系数矩阵

在曲线方程上取点的坐标的过程中,
我们直接为x取自然数的位置来计算 y 的值: 1, 2, 3...:

<img src="https://www.zhihu.com/equation?tex=y_1%20%3D%20d_1%20%2B%20d_2%20%C2%B7%201%20%2B%20d_3%20%C2%B7%201%5E2%20%2B%20..%20%2B%20d_k%20%C2%B7%201%5E%7Bk-1%7D%20%5C%5Cy_2%20%3D%20d_1%20%2B%20d_2%20%C2%B7%202%20%2B%20d_3%20%C2%B7%202%5E2%20%2B%20..%20%2B%20d_k%20%C2%B7%202%5E%7Bk-1%7D%20%5C%5Cy_3%20%3D%20d_1%20%2B%20d_2%20%C2%B7%203%20%2B%20d_3%20%C2%B7%203%5E2%20%2B%20..%20%2B%20d_k%20%C2%B7%203%5E%7Bk-1%7D%20%5C%5C...%20%5C%5C%5C%5C" alt="y_1 = d_1 + d_2 · 1 + d_3 · 1^2 + .. + d_k · 1^{k-1} \\y_2 = d_1 + d_2 · 2 + d_3 · 2^2 + .. + d_k · 2^{k-1} \\y_3 = d_1 + d_2 · 3 + d_3 · 3^2 + .. + d_k · 3^{k-1} \\... \\\\" class="ee_img tr_noresize" eeimg="1">

把上面等式写成矩阵的形式, 得到EC校验块的 **生成矩阵** [Generator-Matrix](https://en.wikipedia.org/wiki/Generator_matrix):

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bbmatrix%7Dy_1%20%5C%5Cy_2%20%5C%5Cy_3%20%5C%5C...%20%5C%5Cy_m%5Cend%7Bbmatrix%7D%20%3D%5Cbegin%7Bbmatrix%7D1%20%20%20%26%201%20%20%20%26%201%5E2%20%26%20...%20%26%201%5E%7Bk-1%7D%20%5C%5C1%20%20%20%26%202%20%20%20%26%202%5E2%20%26%20...%20%26%202%5E%7Bk-1%7D%20%5C%5C1%20%20%20%26%203%20%20%20%26%203%5E2%20%26%20...%20%26%203%5E%7Bk-1%7D%20%5C%5C...%20%26%20...%20%26%20...%20%26%20...%20%26%20...%20%20%20%20%20%5C%5C1%20%20%20%26%20m%20%20%20%26%20m%5E2%20%26%20...%20%26%20m%5E%7Bk-1%7D%5Cend%7Bbmatrix%7D%5Ctimes%5Cbegin%7Bbmatrix%7Dd_1%20%5C%5Cd_2%20%5C%5Cd_3%20%5C%5C...%20%5C%5Cd_k%5Cend%7Bbmatrix%7D%5C%5C" alt="\begin{bmatrix}y_1 \\y_2 \\y_3 \\... \\y_m\end{bmatrix} =\begin{bmatrix}1   & 1   & 1^2 & ... & 1^{k-1} \\1   & 2   & 2^2 & ... & 2^{k-1} \\1   & 3   & 3^2 & ... & 3^{k-1} \\... & ... & ... & ... & ...     \\1   & m   & m^2 & ... & m^{k-1}\end{bmatrix}\times\begin{bmatrix}d_1 \\d_2 \\d_3 \\... \\d_k\end{bmatrix}\\" class="ee_img tr_noresize" eeimg="1">

这里 <img src="https://www.zhihu.com/equation?tex=%20y_1%2C%20y_2%20...%20y_m%20" alt=" y_1, y_2 ... y_m " class="ee_img tr_noresize" eeimg="1"> 就是校验块的数据,
矩阵里就是我们上面使用的这样那组系数.

**这个矩阵就是著名的 [Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix) 矩阵**.

> [Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix) 矩阵只是 EC 其中1种系数的选择方式.
> 其他常用的系数矩阵还有 [Cauchy](https://en.wikipedia.org/wiki/Cauchy_matrix) 矩阵等.


<a class="md-anchor" name="ec解码过程-求解n元一次方程组"></a>

# EC解码过程: 求解n元一次方程组

现在我们知道, EC 就是:

有1组数字:
<img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%2C%20d_3...d_k%20" alt=" d_1, d_2, d_3...d_k " class="ee_img tr_noresize" eeimg="1">
另外记录m个校验用的数字 
<img src="https://www.zhihu.com/equation?tex=%20y_1%2C%20y_2%2C%20y_3...y_m%20" alt=" y_1, y_2, y_3...y_m " class="ee_img tr_noresize" eeimg="1">
使得这k+m个数字中任意丢失m个都能从剩下的k个中恢复所有的k+m个数字.

EC生成校验块的过程称之为EC的**编码**, 当数据丢失需要找回的时候,
使用的是EC的**解码**过程.

如上面章节所说, EC的编码过程是**编码矩阵**([Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix))和数据块列相乘:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bbmatrix%7D1%20%26%201%20%26%201%20%26%20...%20%26%201%20%5C%5C1%20%26%202%20%26%204%20%26%20...%20%26%202%5E%7Bk-1%7D%20%5C%5C1%20%26%203%20%26%209%20%26%20...%20%26%203%5E%7Bk-1%7D%20%5C%5C...%20%5C%5C1%20%26%20m%20%26%20m%5E1%20%26%20...%20%26%20m%5E%7Bk-1%7D%5Cend%7Bbmatrix%7D%5Ctimes%5Cbegin%7Bbmatrix%7Dd_1%20%5C%5Cd_2%20%5C%5Cd_3%20%5C%5C...%20%5C%5Cd_k%5Cend%7Bbmatrix%7D%20%3D%5Cbegin%7Bbmatrix%7Dy_1%20%5C%5Cy_2%20%5C%5Cy_3%20%5C%5C...%20%5C%5Cy_m%5Cend%7Bbmatrix%7D%5C%5C" alt="\begin{bmatrix}1 & 1 & 1 & ... & 1 \\1 & 2 & 4 & ... & 2^{k-1} \\1 & 3 & 9 & ... & 3^{k-1} \\... \\1 & m & m^1 & ... & m^{k-1}\end{bmatrix}\times\begin{bmatrix}d_1 \\d_2 \\d_3 \\... \\d_k\end{bmatrix} =\begin{bmatrix}y_1 \\y_2 \\y_3 \\... \\y_m\end{bmatrix}\\" class="ee_img tr_noresize" eeimg="1">

解码的过程如下:

假设有q个数字丢失了, <img src="https://www.zhihu.com/equation?tex=%20q%20%5Cle%20m%20" alt=" q \le m " class="ee_img tr_noresize" eeimg="1">.
从上面的**编码矩阵**中选择 <img src="https://www.zhihu.com/equation?tex=%20y_1%2C%20y_2..y_q%20" alt=" y_1, y_2..y_q " class="ee_img tr_noresize" eeimg="1">, q行,
组成的一次方程组, 求解丢失的数据.

例如 <img src="https://www.zhihu.com/equation?tex=%20d_2%2C%20d_3%20" alt=" d_2, d_3 " class="ee_img tr_noresize" eeimg="1"> 丢失了, 下面用 <img src="https://www.zhihu.com/equation?tex=%20u_2%2C%20u_3%20" alt=" u_2, u_3 " class="ee_img tr_noresize" eeimg="1"> 表示
(只丢失了2块数据, 不需要所有的m个校验块参与, 只需要2个校验块来恢复数据)

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bbmatrix%7D1%20%26%202%20%26%204%20%26%20...%20%26%202%5E%7Bk-1%7D%20%5C%5C1%20%26%203%20%26%209%20%26%20...%20%26%203%5E%7Bk-1%7D%20%5C%5C%5Cend%7Bbmatrix%7D%5Ctimes%5Cbegin%7Bbmatrix%7Dd_1%20%5C%5Cu_2%20%5C%5Cu_3%20%5C%5C...%20%5C%5Cd_k%5Cend%7Bbmatrix%7D%20%3D%5Cbegin%7Bbmatrix%7Dy_2%20%5C%5Cy_3%20%5C%5C%5Cend%7Bbmatrix%7D%5C%5C" alt="\begin{bmatrix}1 & 2 & 4 & ... & 2^{k-1} \\1 & 3 & 9 & ... & 3^{k-1} \\\end{bmatrix}\times\begin{bmatrix}d_1 \\u_2 \\u_3 \\... \\d_k\end{bmatrix} =\begin{bmatrix}y_2 \\y_3 \\\end{bmatrix}\\" class="ee_img tr_noresize" eeimg="1">

这个矩阵表示的方程组里有2个未知数 <img src="https://www.zhihu.com/equation?tex=%20u_2%2C%20u_3%20" alt=" u_2, u_3 " class="ee_img tr_noresize" eeimg="1">,
解方程即可得到 <img src="https://www.zhihu.com/equation?tex=%20u_2%2C%20u_3%20" alt=" u_2, u_3 " class="ee_img tr_noresize" eeimg="1"> 这2块丢失的数据.

<a class="md-anchor" name="vandermonde-矩阵保证方程组有解"></a>

## [Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix)
 矩阵保证方程组有解

对于k+m的EC来说, 任意丢失m个数据块都可以将其找回.

[Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix) 矩阵保证了任意`m`行`m`列组成的子矩阵都是线性无关的,
构成的方程肯定有确定解.

<img src="https://www.zhihu.com/equation?tex=V%3D%5Cbegin%7Bbmatrix%7D1%20%20%20%20%20%20%26%20%5Calpha_1%20%26%20%5Calpha_1%5E2%20%26%20%5Cdots%20%20%26%20%5Calpha_1%5E%7Bn-1%7D%20%20%20%20%5C%5C1%20%20%20%20%20%20%26%20%5Calpha_2%20%26%20%5Calpha_2%5E2%20%26%20%5Cdots%20%20%26%20%5Calpha_2%5E%7Bn-1%7D%20%20%20%20%5C%5C1%20%20%20%20%20%20%26%20%5Calpha_3%20%26%20%5Calpha_3%5E2%20%26%20%5Cdots%20%20%26%20%5Calpha_3%5E%7Bn-1%7D%20%20%20%20%5C%5C%5Cvdots%20%26%20%5Cvdots%20%20%20%26%20%5Cvdots%20%20%20%20%20%26%20%5Cddots%20%26%20%5Cvdots%20%20%20%20%20%20%20%20%20%20%20%20%5C%5C1%20%20%20%20%20%20%26%20%5Calpha_m%20%26%20%5Calpha_m%5E2%20%26%20%5Cdots%20%20%26%20%5Calpha_m%5E%7Bn-1%7D%5Cend%7Bbmatrix%7D%5C%5C" alt="V=\begin{bmatrix}1      & \alpha_1 & \alpha_1^2 & \dots  & \alpha_1^{n-1}    \\1      & \alpha_2 & \alpha_2^2 & \dots  & \alpha_2^{n-1}    \\1      & \alpha_3 & \alpha_3^2 & \dots  & \alpha_3^{n-1}    \\\vdots & \vdots   & \vdots     & \ddots & \vdots            \\1      & \alpha_m & \alpha_m^2 & \dots  & \alpha_m^{n-1}\end{bmatrix}\\" class="ee_img tr_noresize" eeimg="1">

[Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix) 的 行列式的值为:

<img src="https://www.zhihu.com/equation?tex=%5Cdet%28V%29%3D%5Cprod_%7B1%20%5Cleq%20i%20%5Clt%20j%20%5Cleq%20n%7D%28%5Calpha_j%20-%20%5Calpha_i%29%5C%5C" alt="\det(V)=\prod_{1 \leq i \lt j \leq n}(\alpha_j - \alpha_i)\\" class="ee_img tr_noresize" eeimg="1">

只要 <img src="https://www.zhihu.com/equation?tex=%20%5Calpha_i%20" alt=" \alpha_i " class="ee_img tr_noresize" eeimg="1"> 都不同, 则 [Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix) 矩阵的行列式就不为0,
矩阵可逆, 表示方程有唯一解.

容易证明, [Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix) 矩阵的任意 <img src="https://www.zhihu.com/equation?tex=%20m%20%5Ctimes%20m%20" alt=" m \times m " class="ee_img tr_noresize" eeimg="1">的子矩阵也可以保证永远有唯一解.

> 到此为止我们讨论了EC在有理数范围内的全部内容.
> 它是完整的, 但还不能直接应用到计算机的代码开发商.
> 
> 接下来我们要展开在纯数学和计算机算法之间的问题,
> 以及我们将通过什么样的手段来解决这些问题, 将EC真正应用到生产环境中.


<a name="ec-gf7"></a>

<a class="md-anchor" name="新世界-伽罗华域-galois-field-gf7"></a>

# 新世界: 伽罗华域 
[Galois-Field](https://en.wikipedia.org/wiki/Finite_field)
 GF(7)

在实际使用中, 并不像上面的有理数计算那么简单:
就像所有算法在实现中多会面临的问题一样, 在计算机上实现, 必须考虑空间问题.
计算机里不能天然的表示任意自然数,
上面的校验块 <img src="https://www.zhihu.com/equation?tex=%20y_i%20" alt=" y_i " class="ee_img tr_noresize" eeimg="1"> 在计算过程中必然会出现越界问题.

<img src="https://www.zhihu.com/equation?tex=y%20%3D%20d_1%20%2B%20d_2%20x%20%2B%20d_3%20x%5E2%20%2B%20...%20%2B%20d_k%20x%5E%7Bk-1%7D%5C%5C" alt="y = d_1 + d_2 x + d_3 x^2 + ... + d_k x^{k-1}\\" class="ee_img tr_noresize" eeimg="1">

如果我们的数据块 <img src="https://www.zhihu.com/equation?tex=%20d_j%20" alt=" d_j " class="ee_img tr_noresize" eeimg="1"> 的取值范围是1个字节大小,
那么计算出来的校验数据 <img src="https://www.zhihu.com/equation?tex=%20y_i%20" alt=" y_i " class="ee_img tr_noresize" eeimg="1"> 随着x的值的选取, 很可能就超出了1个字节大小,
如果仍然使用这种方式生成校验块, **最终冗余的数据的大小就会变得不可控**,
实际存储的冗余会大于 `k+m : k` 的冗余度, 无法达到有效控制冗余数据大小的目的.

因此上面介绍的EC, 在计算机上实现时,
必须解决数字大小的问题. 
但总的算法是不变的. 这次我们要从最底层开始入手, 解决这个问题.

**这里所说的最底层, 是指曲线, 多元一次方程等依赖的底层的四则运算法则.
我们将找到另外一套四则运算, 既能满足 EC 计算的需要,
又能很好第控制数值的范围.
我们要将 EC 移植到另一套代数结构上**.

> 这也是我自己在学习 EC 时觉得最有趣的地方:
> 
> 类似于把一段c代码写好后可以编译到intel CPU上也可以编译到ARM
> CPU上运行(即使这2种CPU的指令完全不同, 但c源代码的正确性是不变的),
> 
> 现在我们要做的是, 我们设计好 EC 的上层算法后,
> 把它移植到另1套代数体系中, 而同时也能保证它上层的"源代码"
> 在另1种不同的底层体系上也可以正确运行!


<a class="md-anchor" name="ec在计算机里的实现-基于-伽罗华域-galois-field"></a>

## EC在计算机里的实现: 基于 伽罗华域 
[Galois-Field](https://en.wikipedia.org/wiki/Finite_field)

上面我们提到的几个数学公式, 高次曲线, 多元一次方程组等:
<img src="https://www.zhihu.com/equation?tex=%20y%20%3D%20d_1%20%2B%20d_2%20x%20%2B%20d_3%20x%5E2%20%2B%20...%20%2B%20d_k%20x%5E%7Bk-1%7D%20" alt=" y = d_1 + d_2 x + d_3 x^2 + ... + d_k x^{k-1} " class="ee_img tr_noresize" eeimg="1">

他们之所以能正确的工作, 是因为他们依赖于一套底层的基础运算规则,
这就是四则运算: <img src="https://www.zhihu.com/equation?tex=%20%2B%20-%20%5Ctimes%20%5Cdiv%20" alt=" + - \times \div " class="ee_img tr_noresize" eeimg="1">
(实现 EC 的代数中我们没有用到开方运算).

**这听起来有点废话, ™不用四则运算用什么**?

其实我们平时熟知的四则运算, 在代数里并不是唯一的四则运算法则,
它有很多很多个兄弟, 他们有共同的规律,却有着不同的表现形式.

例如在有1种四则运算建立的代数可能是: 
<img src="https://www.zhihu.com/equation?tex=%205%20%2B%205%20%3D%203%20" alt=" 5 + 5 = 3 " class="ee_img tr_noresize" eeimg="1"> 而不是10,
<img src="https://www.zhihu.com/equation?tex=%205%20%5Ctimes%203%20%3D%201%20" alt=" 5 \times 3 = 1 " class="ee_img tr_noresize" eeimg="1"> 而不是15.
也可能有1种四则运算里乘法不是加法的叠加.

> 最常见的是钟表的时间相加, 20点加8个小时不是28点, 而是4点.


我们现在需要做的是, 找到一种四则运算, 来让 EC 的计算可以不会越界!

现在我们来一步步开启这扇新世界的大门...

首先感谢19世纪因为跟情敌决斗被一枪打死的伟大数学家 伽罗华.

<a class="md-anchor" name="栗子3-只有7个数字的新世界-gf7"></a>

## 栗子🌰3: 只有7个数字的新世界: GF(7)

大门, 慢慢开启...

我们来尝试定义一个新的加法规则, 在这个新的世界里只有0~6这7个数字:

其他整数进来时都要被模7, 变成0~6的数字.

在这个模7的新世界里, 四则运算也可以工作:

<a class="md-anchor" name="模7新世界中的-加法"></a>

### 模7新世界中的 
**加法**

我们来尝试定义一个新的加法规则, 在这个只有0~6这7个数字的新世界里,
(新的加法被表示为 ⊕ (这里原始的加法还是用`+`来表示)):

<img src="https://www.zhihu.com/equation?tex=a%20%E2%8A%95%20b%20%5Crightarrow%20%28a%20%2B%20b%29%20%5Cpmod%207%5C%5C" alt="a ⊕ b \rightarrow (a + b) \pmod 7\\" class="ee_img tr_noresize" eeimg="1">

它定义为: a ⊕ b的结果是 a + b后结果再对7取模.
例如:

1 ⊕ 1 = 2 <br/>
5 ⊕ 2 = 0 ( 7 % 7 = 0 ) <br/>
5 ⊕ 5 = 3 ( 10 % 7 = 3 )

在这个新世界里, 0 还是和以前的0很相像, 任何数跟0相加都不变:

0 ⊕ 3 = 3 <br/>
2 ⊕ 0 = 2

0 在新世界 GF(7) 里被称为加法的**单位元**.

<a class="md-anchor" name="模7新世界中的-减法"></a>

### 模7新世界中的 
**减法**

然后我们再在模7的世界里定义减法.
减法的定义也很直接, 就是加法的逆运算了.

就像自然数里1样, -2 + 2 = 0, 我们称呼-2是2在加法上的逆元(通常称为`相反数`).
在模7的世界里,我们也很容易找到每个数的加法逆元,例如:
<img src="https://www.zhihu.com/equation?tex=%203%20%E2%8A%95%204%20%3D%200%20" alt=" 3 ⊕ 4 = 0 " class="ee_img tr_noresize" eeimg="1">
所以 4 和 3 就互为加法的逆元, 或者说是(新世界的)`相反数`.

减法定义就是: <img src="https://www.zhihu.com/equation?tex=%20a%20%E2%8A%96%20b%20%5Crightarrow%20a%20%E2%8A%95%20%28-b%29%20" alt=" a ⊖ b \rightarrow a ⊕ (-b) " class="ee_img tr_noresize" eeimg="1">.

例如:

3 ⊖ 4 = 6 ( (-1) % 7 = 6 ) <br/>
2 ⊖ 6 = 3 ( (-4) % 7 = 3 )

> 其实我们不需要减法, 我们只需要 加法 和 逆元 的定义


<a class="md-anchor" name="模7新世界中的-乘法-和-除法"></a>

### 模7新世界中的 
**乘法**
 和 
**除法**

在模7的新世界里, 我们也可以类似地定义1个乘法:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bequation%7Da%20%E2%8A%97%20b%20%5Crightarrow%20%28a%20%5Ctimes%20b%29%20%5Cmod%207%5Cend%7Bequation%7D%5C%5C" alt="\begin{equation}a ⊗ b \rightarrow (a \times b) \mod 7\end{equation}\\" class="ee_img tr_noresize" eeimg="1">

例如:

1 ⊗ 5 = 5 ( 5 % 7 = 5 ) <br/>
3 ⊗ 4 = 5 ( 12 % 7 = 5 ) <br/>
2 ⊗ 5 = 3 ( 10 % 7 = 3 ) <br/>
0 ⊗ 6 = 0

对于模7新世界的乘法⊗来说, 1 是乘法的**单位元**,
也就是说1 ⊗ 任何数都是它本身.

我们也可以用类似的方法定义每个数字在乘法⊗的逆元:

a的乘法逆元 <img src="https://www.zhihu.com/equation?tex=%20a%5E%7B-1%7D%20%3D%20b%2C%20iff%20a%20%E2%8A%97%20b%20%3D%201%20" alt=" a^{-1} = b, iff a ⊗ b = 1 " class="ee_img tr_noresize" eeimg="1">.

例如:

$$
\begin{aligned}
3^{-1} & = 5 ( 3 \times 5 % 7 = 1 ) \\
4^{-1} & = 2 ( 4 \times 2 % 7 = 1 )
\end{aligned}
$$

除法的定义就是: 乘以它的乘法逆元

<a class="md-anchor" name="栗子4-模7新世界直线方程-1"></a>

## 栗子🌰4: 模7新世界直线方程-1

现在我们有了新的加法和减法⊕, ⊖ 我们可以像使用旧世界的加减法一样来使用⊕, ⊖.
例如我们可以建立一个简单的, 斜率为1的直线方程:

<img src="https://www.zhihu.com/equation?tex=y%20%3D%20x%20%E2%8A%95%203%5C%5C" alt="y = x ⊕ 3\\" class="ee_img tr_noresize" eeimg="1">

新世界里这个直线上的点是:
(x,y) ∈ [(0,3), (1,4), (2,5), (3,6), (4,0), (5,1), (6,2)]
只有7个.

如果把这条直线画到坐标系里, 它应该是这个样子的:

```
y = x ⊕ 3

  y
  ^
6 |     •
5 |   •
4 | •
3 •
2 |           •
1 |         •
0 +-------•-----> x
  0 1 2 3 4 5 6 

```

<a class="md-anchor" name="栗子5-模7新世界直线方程-2"></a>

## 栗子🌰5: 模7新世界直线方程-2

再加上新世界加减乘除四则运算, 我们可以在新世界里进行基本的代数运算了,
例如我们可以设定1个斜率为2的直线方程:

<img src="https://www.zhihu.com/equation?tex=y%20%3D%202%20%E2%8A%97%20x%20%E2%8A%95%203%5C%5C" alt="y = 2 ⊗ x ⊕ 3\\" class="ee_img tr_noresize" eeimg="1">

新世界里这个直线上的点是:
(x,y) ∈ [(0,3), (1,5), (2,0), (3,2), (4,4), (5,6), (6,1)]
这7个.

如果把这条直线画到坐标系里, 它应该是这个样子的:

```
y = 2 ⊗ x ⊕ 3

  y
  ^
6 |          •
5 | •
4 |       •
3 •
2 |     •
1 |           •
0 +---•---------> x
  0 1 2 3 4 5 6 
```

<a class="md-anchor" name="栗子6-模7新世界中的二次曲线方程"></a>

## 栗子🌰6: 模7新世界中的二次曲线方程

下面我们来建立1个稍微复杂1点的, 二次曲线的方程:

<img src="https://www.zhihu.com/equation?tex=y%20%3D%20x%5E2%20%E2%8A%95%20x%20%E2%8A%95%202%5C%5C" alt="y = x^2 ⊕ x ⊕ 2\\" class="ee_img tr_noresize" eeimg="1">

这里 <img src="https://www.zhihu.com/equation?tex=%20x%5E2%20" alt=" x^2 " class="ee_img tr_noresize" eeimg="1"> 表示 <img src="https://www.zhihu.com/equation?tex=%20x%20%E2%8A%97%20x%20" alt=" x ⊗ x " class="ee_img tr_noresize" eeimg="1">

新世界里这个抛物线上的点集合是:
(x,y) ∈ [(0, 2) (1, 4) (2, 1) (3, 0) (4, 1) (5, 4) (6, 2)]

如果把这条抛物线画到坐标系里, 它应该是这个样子的:

```
y = x^2 ⊕ x ⊕ 2

  y
  ^
6 |
5 |
4 | •       •
3 |
2 •           •
1 |   •   •
0 +-----•-------> x
  0 1 2 3 4 5 6
```

可以看出它的图像也遵循了旧世界抛物线的特性: **这条抛物线是以3为轴对称的**:
因为类似旧世界的多项式分解一样, 原方程也可以分解成:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Baligned%7Dy%20%26%20%3D%20%28x%20%E2%8A%95%20%28-3%29%29%5E2%20%5C%5C%20%20%26%20%3D%20x%5E2%20%E2%8A%95%20%28-6%29x%20%E2%8A%95%209%20%5C%5C%20%20%26%20%3D%20x%5E2%20%E2%8A%95%20x%20%E2%8A%95%202%5Cend%7Baligned%7D%5C%5C" alt="\begin{aligned}y & = (x ⊕ (-3))^2 \\  & = x^2 ⊕ (-6)x ⊕ 9 \\  & = x^2 ⊕ x ⊕ 2\end{aligned}\\" class="ee_img tr_noresize" eeimg="1">

<a class="md-anchor" name="模7新世界里的ec"></a>

## 模7新世界里的EC

在这个模7的新世界里, 它满足我们旧世界里的四则运算法则,
我们已经可以使用上面提到的 EC 的算法来编码或解码了:

假设模7新世界里我们的数据块 <img src="https://www.zhihu.com/equation?tex=%20d_1%20%3D%203%2C%20d_2%20%3D%202%20" alt=" d_1 = 3, d_2 = 2 " class="ee_img tr_noresize" eeimg="1">, 对应上面的直线方程:
y = 2 ⊗ x ⊕ 3

我们只要记住2个点的位置, 就能把直线的方程恢复出来:

例如:

-   我们先记录直线上2个点:
    (1,5) 和 (3,2)

-   假设丢失的数据是 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%20" alt=" d_1, d_2 " class="ee_img tr_noresize" eeimg="1"> 用 <img src="https://www.zhihu.com/equation?tex=%20u_1%2C%20u_2%20" alt=" u_1, u_2 " class="ee_img tr_noresize" eeimg="1"> 表示, 带入2个点的坐标,
    得到一个二元一次方程组:

    <img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bcases%7D%5Cbegin%7Baligned%7D5%20%26%20%3D%20u_2%20%E2%8A%95%20u_1%20%5C%5C2%20%26%20%3D%20u_2%20%E2%8A%97%203%20%E2%8A%95%20u_1%5Cend%7Baligned%7D%5Cend%7Bcases%7D%5C%5C" alt="\begin{cases}\begin{aligned}5 & = u_2 ⊕ u_1 \\2 & = u_2 ⊗ 3 ⊕ u_1\end{aligned}\end{cases}\\" class="ee_img tr_noresize" eeimg="1">

    2个方程左右分别相减消元:

    <img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Baligned%7D5%20%E2%8A%95%20%28-2%29%20%26%20%3D%20u_2%20%E2%8A%97%20%281%20%E2%8A%95%20%28-3%29%29%20%E2%8A%95%20u_1%20%E2%8A%95%20%28-u_1%29%20%5C%5C%20%20%205%20%E2%8A%95%205%20%26%20%3D%20u_2%20%E2%8A%97%20%281%20%E2%8A%95%204%29%20%5C%5C%20%20%20%20%20%20%203%20%26%20%3D%20u_2%20%E2%8A%97%205%5Cend%7Baligned%7D%5C%5C" alt="\begin{aligned}5 ⊕ (-2) & = u_2 ⊗ (1 ⊕ (-3)) ⊕ u_1 ⊕ (-u_1) \\   5 ⊕ 5 & = u_2 ⊗ (1 ⊕ 4) \\       3 & = u_2 ⊗ 5\end{aligned}\\" class="ee_img tr_noresize" eeimg="1">

    最后得到 <img src="https://www.zhihu.com/equation?tex=%20u_2%20%3D%203%20%E2%8A%97%205%5E%7B-1%7D%20%3D%203%20%E2%8A%97%203%20%3D%202%20" alt=" u_2 = 3 ⊗ 5^{-1} = 3 ⊗ 3 = 2 " class="ee_img tr_noresize" eeimg="1">.

    将<img src="https://www.zhihu.com/equation?tex=%20u_2%20%3D%202%20" alt=" u_2 = 2 " class="ee_img tr_noresize" eeimg="1"> 带入第1个方程:

    <img src="https://www.zhihu.com/equation?tex=%205%20%3D%202%20%E2%8A%97%201%20%E2%8A%95%20u_1%20%5C%5C" alt=" 5 = 2 ⊗ 1 ⊕ u_1 \\" class="ee_img tr_noresize" eeimg="1">

    得到 <img src="https://www.zhihu.com/equation?tex=%20u_1%20" alt=" u_1 " class="ee_img tr_noresize" eeimg="1">:

    <img src="https://www.zhihu.com/equation?tex=%20u_1%20%3D%205%20%E2%8A%95%20%28-2%29%20%3D%203%20%5C%5C" alt=" u_1 = 5 ⊕ (-2) = 3 \\" class="ee_img tr_noresize" eeimg="1">

至此, 我们用模7新世界的四则运算实现了之前的 EC . 并且我们保证了校验数据的大小是可控的:
不会大于7!
距离我们的目标又接近了1步.

类似的, 我们可以通过模7新世界的抛物线, 来实现k=3, k=4的 EC.

> NOTE: <br/>
> 模7下的四则运算构成了1个 伽罗华域 [Galois-Field](https://en.wikipedia.org/wiki/Finite_field): <img src="https://www.zhihu.com/equation?tex=%20GF%287%29%20" alt=" GF(7) " class="ee_img tr_noresize" eeimg="1">.
> 
> 模7是1个可选的数, 也可以选择模11或其他质数来构造1个 [Galois-Field](https://en.wikipedia.org/wiki/Finite_field),
> 但是不能选择模一个合数来建立新的四则运算规则.
> 假设使用模6, 模6世界里面的2是6的一个因子, 它没有乘法逆元, 也即是说2 乘以
> 1~5任何一个数在模6的世界里都不是1.
> 
> 没有乘法逆元就说明模6的世界里没有和旧世界里一样的除法,
> 不能构成一个完整的四则运算体系.


> NOTE: <br/>
> 为了简化本文, 四则里还有几个方面没有提到, 例如乘法加法的分配率.
> 乘法和加法的结合律也必须满足, 才能在新世界里实现上面例子中的曲线方程等元素.
> 这部分也很容验证,在上面的模7新世界里是可以满足的.


现在我们有了 EC 的算法,
以及很多个可以选择的四则运算来限定数值的范围.
接下来要在计算机上实现,还有1步,就是:
模7虽然可取,但是它没有办法对计算机里的数字有效利用,因为计算机里的数是二进制的.
如果把数值限定到7或其他质数上,没有办法实现256或65536这样的区间的有效利用.

所以接下来我们需要在所有四则运算里选择一个符合计算机的二进制的四则运算,
作为实现 EC 计算的基础代数结构.

<a name="#ec-gf256"></a>

<a class="md-anchor" name="ec使用的新世界-galois-field-gf256"></a>

# EC使用的新世界 
[Galois-Field](https://en.wikipedia.org/wiki/Finite_field)
 GF(256)

从现在开始, 我们要构造一个现实中真实可以用的伽罗华域,
它比上面模7新世界稍微复杂一点, 得到这个域分为2步:

-   我们首先选择1个基础的,
    只包含2个元素的 [Galois-Field](https://en.wikipedia.org/wiki/Finite_field) <img src="https://www.zhihu.com/equation?tex=%20GF%282%29%20" alt=" GF(2) " class="ee_img tr_noresize" eeimg="1">: {0, 1}.

-   再在这个 <img src="https://www.zhihu.com/equation?tex=%20GF%282%29%20" alt=" GF(2) " class="ee_img tr_noresize" eeimg="1"> 的基础上建立1个有256个元素的 [Galois-Field](https://en.wikipedia.org/wiki/Finite_field) <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E8%29%20" alt=" GF(2^8) " class="ee_img tr_noresize" eeimg="1">.

<a class="md-anchor" name="模2的新世界-galois-field-gf2"></a>

## 模2的新世界: 
[Galois-Field](https://en.wikipedia.org/wiki/Finite_field)
 GF(2)

首先我们要构建一个最基础的四则运算, 我们先选择了最小的1个[Galois-Field](https://en.wikipedia.org/wiki/Finite_field),
里面只有2个元素{0,1}:

在这个GF(2)里, 运算的规则也非常简单:

-   加法(刚好和位运算的`异或`等价):

    0 ⊕ 0 = 0 <br/>
    0 ⊕ 1 = 1 <br/>
    1 ⊕ 0 = 1 <br/>
    1 ⊕ 1 = 0

    1的加法逆元就是1 本身.

-   乘法(刚好和位运算的`与`等价):

    0 ⊗ 0 = 0 <br/>
    0 ⊗ 1 = 0 <br/>
    1 ⊗ 0 = 0 <br/>
    1 ⊗ 1 = 1

    1的乘法逆元就是1 本身. 0 没有乘法逆元.

> 以这个GF(2)为基础, 我们已经可以构建一个1-bit的 EC 算法了:)


下一步我们希望构建1个1 byte大小(<img src="https://www.zhihu.com/equation?tex=%202%5E8%20" alt=" 2^8 " class="ee_img tr_noresize" eeimg="1"> 个元素)的 [Galois-Field](https://en.wikipedia.org/wiki/Finite_field) <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E8%29%20" alt=" GF(2^8) " class="ee_img tr_noresize" eeimg="1">,
在这个 <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E8%29%20" alt=" GF(2^8) " class="ee_img tr_noresize" eeimg="1"> 里的 EC 中,
的每个<img src="https://www.zhihu.com/equation?tex=%20d_j%20" alt=" d_j " class="ee_img tr_noresize" eeimg="1"> 和 <img src="https://www.zhihu.com/equation?tex=%20y_i%20" alt=" y_i " class="ee_img tr_noresize" eeimg="1">的取值范围可以是0~255.

有点类似于把0~9这10个自然数通过增加进位这个概念后
扩展成能表示任意大小的多位的10进制自然数,
我们通过类似的方法把{0,1}这个<img src="https://www.zhihu.com/equation?tex=%20GF%282%29%20" alt=" GF(2) " class="ee_img tr_noresize" eeimg="1"> 扩大,
引入多项式:

我们使用 GF(2) 的元素作为系数, 定义1个多项式:

<img src="https://www.zhihu.com/equation?tex=a_n%20x%5En%20%2B%20...%20%2B%20a_2%20x%5E2%20%2B%20a_1%20x%5E1%20%2B%20a_0%20%5C%5Ca_i%20%5Cin%20GF%282%29%20%3D%20%5C%7B0%2C1%5C%7D%5C%5C" alt="a_n x^n + ... + a_2 x^2 + a_1 x^1 + a_0 \\a_i \in GF(2) = \{0,1\}\\" class="ee_img tr_noresize" eeimg="1">

<img src="https://www.zhihu.com/equation?tex=%20a_i%20" alt=" a_i " class="ee_img tr_noresize" eeimg="1"> 的四则运算还是遵循 GF(2) 的规则的,
而多项式的四则运算,基于它的系数的四则运算建立:

例如多项式的加法:

-   因为 1 + 1 = 0, 所以:

    <img src="https://www.zhihu.com/equation?tex=%20%28x%20%2B%201%29%20%2B%20%281%29%20%3D%20x%20%5C%5C" alt=" (x + 1) + (1) = x \\" class="ee_img tr_noresize" eeimg="1">

-   x的同指数幂的系数相加遵循系数的Field的加法规则, 1 + 1 = 0:

    <img src="https://www.zhihu.com/equation?tex=%20%28x%5E2%20%2B%20x%20%2B%201%29%20%2B%20%28x%29%20%3D%20x%5E2%20%2B%201%20%5C%5C" alt=" (x^2 + x + 1) + (x) = x^2 + 1 \\" class="ee_img tr_noresize" eeimg="1">

-   2个相同的多项式相加肯定是0:

    <img src="https://www.zhihu.com/equation?tex=%20%28x%5E2%20%2B%20x%20%2B%201%29%20%2B%20%28x%5E2%20%2B%20x%20%2B%201%29%20%3D%200%20%5C%5C" alt=" (x^2 + x + 1) + (x^2 + x + 1) = 0 \\" class="ee_img tr_noresize" eeimg="1">

多项式的乘法和旧世界的多项式乘法类似, 仍然是通过乘法的分配率展开多项式:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Baligned%7D%28x%20%2B%201%29%20%28x%20%2B%201%29%20%26%20%3D%20x%20%28x%2B1%29%20%2B%20%28x%2B1%29%20%5C%5C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%26%20%3D%20x%5E2%20%2B%20x%20%2B%20x%20%2B%201%20%5C%5C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%26%20%3D%20x%5E2%20%2B%201%5Cend%7Baligned%7D%5C%5C" alt="\begin{aligned}(x + 1) (x + 1) & = x (x+1) + (x+1) \\                & = x^2 + x + x + 1 \\                & = x^2 + 1\end{aligned}\\" class="ee_img tr_noresize" eeimg="1">

多项式的除法依旧使用旧世界的多项式长除法法则,
唯一不同仍旧是系数的四则运算是基于GF(2)的:

例如:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Baligned%7D%5Cfrac%7Bx%5E3%20%2B%201%7D%7Bx%20%2B%201%7D%20%3D%20x%5E2%20%2B%20x%20%2B%201%5Cend%7Baligned%7D%5C%5C" alt="\begin{aligned}\frac{x^3 + 1}{x + 1} = x^2 + x + 1\end{aligned}\\" class="ee_img tr_noresize" eeimg="1">

多项式的除法的取余计算也类似:

<img src="https://www.zhihu.com/equation?tex=x%5E2%20%2B%20x%20%2B%201%20%3D%20x%20%28x%2B1%29%20%2B%201%20%5C%5C%28x%5E2%20%2B%20x%20%2B%201%29%20%3D%201%20%5Cpmod%20%28x%2B1%29%5C%5C" alt="x^2 + x + 1 = x (x+1) + 1 \\(x^2 + x + 1) = 1 \pmod (x+1)\\" class="ee_img tr_noresize" eeimg="1">

现在我们通过把 GF(2) 应用到多项式的系数上,
得到了1个包含无限多个元素的多项式的集合
(它还不是一个伽罗华域, 因为缺少除法逆元. 就像整数全集也不是一个伽罗华域,
它也缺少除法逆元),

然后我们还发现, **这些多项式和二进制数是有一一对应关系的**,
多项式中指数为i的项的系数就是二进制数第i位的值:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Baligned%7D%20%20%20%20%20%201%20%26%20%5Crightarrow%20%20%20%201%20%5C%5Cx%5E2%20%2B%201%20%26%20%5Crightarrow%20%20101%20%5C%5Cx%5E3%20%2B%20x%20%26%20%5Crightarrow%201010%5Cend%7Baligned%7D%5C%5C" alt="\begin{aligned}      1 & \rightarrow    1 \\x^2 + 1 & \rightarrow  101 \\x^3 + x & \rightarrow 1010\end{aligned}\\" class="ee_img tr_noresize" eeimg="1">

现在我们可以使用多项式表达的二进制整数的全集.
然后就像上面栗子中的 GF(7) 那样, 通过取模的方式,
将多项式的集合构造1个取模的伽罗华域.

类似的, 现在我们需要找到1个质的多项式([Prime-Polynomial](https://en.wikipedia.org/wiki/Irreducible_polynomial)),
来替代GF(7)中7的角色,
并应用到GF(2)为系数的多项式的集合中,
最终得到1个有256个元素的多项式的伽罗华域 <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E8%29%20" alt=" GF(2^8) " class="ee_img tr_noresize" eeimg="1">.

首先让我们来熟悉下如何从较小的域扩张到较大的域.

<a class="md-anchor" name="域的扩张-field-extension"></a>

## 域的扩张 
[Field-Extension](https://en.wikipedia.org/wiki/Field_extension)

域的扩张大家应该是非常熟悉的,
只是一般并没有用这个专用的称呼去描述我们平时见到的扩展.

域的扩张经常是通过多项式来完成的.

<a class="md-anchor" name="栗子7-实数到虚数的扩张"></a>

### 栗子🌰7: 实数到虚数的扩张

例如我们首先有了实数, 以实数为系数的多项式中,
如果我们选择一个多项式来构造一个方程:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bequation%7Dx%5E2%20%2B%201%20%3D%200%5Cend%7Bequation%7D%5C%5C" alt="\begin{equation}x^2 + 1 = 0\end{equation}\\" class="ee_img tr_noresize" eeimg="1">

这个方程在实数域里是无解的, 但在复数范围内是有解的:
<img src="https://www.zhihu.com/equation?tex=%20x%20%3D%20%5Cpm%20%5Csqrt%7B-1%7D%20%3D%20%5Cpm%20i%20" alt=" x = \pm \sqrt{-1} = \pm i " class="ee_img tr_noresize" eeimg="1">.

这样通过一个实数系数的, 但在实数域中没有根的方程,
我们得到了复数 [Complex-Number](https://en.wikipedia.org/wiki/Irreducible_polynomial#Field_extension) 的定义,

**复数就是: 所有实系数多项式模 <img src="https://www.zhihu.com/equation?tex=%20x%5E2%2B1%20" alt=" x^2+1 " class="ee_img tr_noresize" eeimg="1"> 的余多项式的集合**:

$$
\mathbb {C} =\mathbb {R} [X]/(X^{2}+1).
$$

上面所有的余多项式可以表示为: <img src="https://www.zhihu.com/equation?tex=%20a%20x%20%2B%20b%20" alt=" a x + b " class="ee_img tr_noresize" eeimg="1">, a, b都是实数.

这里<img src="https://www.zhihu.com/equation?tex=%20a%20x%20%2B%20b%20" alt=" a x + b " class="ee_img tr_noresize" eeimg="1"> 就是我们熟悉的复数:
多项式 x 对应虚数单位i, 1对应实数单位1.

而任意2个多项式的四则运算, 也对应复数的四则运算, 
例如, 设: <img src="https://www.zhihu.com/equation?tex=%20p%28x%29%20%3D%20x%5E2%20%2B%201%20" alt=" p(x) = x^2 + 1 " class="ee_img tr_noresize" eeimg="1">

<table>
<tr class="header">
<th style="text-align: left;">多项式(<br /><span class="math display">$$ \pmod{p(x)} $$</span><br />)</th>
<th style="text-align: left;">复数</th>
</tr>
<tr class="odd">
<td style="text-align: left;"><br /><span class="math display"><em>x</em> + (<em>x</em> + 1) = 2<em>x</em> + 1</span><br /></td>
<td style="text-align: left;"><br /><span class="math display"><em>i</em> + (1 + <em>i</em>) = 1 + 2<em>i</em></span><br /></td>
</tr>
<tr class="even">
<td style="text-align: left;"><br /><span class="math display"><em>x</em> · <em>x</em> =  − 1</span><br /></td>
<td style="text-align: left;"><br /><span class="math display"><em>i</em> · <em>i</em> =  − 1</span><br /></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><br /><span class="math display">(3<em>x</em> + 1) · (<em>x</em> − 2) =  − 5<em>x</em> − 5</span><br /></td>
<td style="text-align: left;"><br /><span class="math display">(1 + 3<em>i</em>) · ( − 2 + <em>i</em>) =  − 5 − 5<em>i</em></span><br /></td>
</tr>
</table>

**类似于将实数扩张到复数, 我们也可以将GF(2) 扩张到 <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E8%29%20" alt=" GF(2^8) " class="ee_img tr_noresize" eeimg="1">**.

<a class="md-anchor" name="从2到256-扩张-gf2"></a>

## 从2到256: 扩张 GF(2)

域的扩张就是在现有域为系数的多项式中, 找到1个质的多项式 [Prime-Polynomial](https://en.wikipedia.org/wiki/Irreducible_polynomial),
再将所有多项式模它得到的结果的集合就是域的扩张.

例如 <img src="https://www.zhihu.com/equation?tex=%20x%5E2%20%2B%201%20" alt=" x^2 + 1 " class="ee_img tr_noresize" eeimg="1"> 在实数域下就是 **质多项式**, 它无法分解成2个多项式乘积.

<a class="md-anchor" name="栗子8-gf2-下的质多项式"></a>

### 栗子🌰8: GF(2) 下的质多项式

-   1 是1个质多项式.

-   <img src="https://www.zhihu.com/equation?tex=%20x%20%2B%201%20" alt=" x + 1 " class="ee_img tr_noresize" eeimg="1"> 是1个质多项式.
    因为它最高次幂是1, 肯定不能再拆分成2个多项式乘积了(只能拆分成1次多项式和常数的乘积).

-   2次的质多项式是: <img src="https://www.zhihu.com/equation?tex=%20P_2%28x%29%20%3D%20x%5E2%20%2B%20x%20%2B%201%20" alt=" P_2(x) = x^2 + x + 1 " class="ee_img tr_noresize" eeimg="1">.
    它在GF(2)的域中不能被拆分成2个1次多项式的乘积.

    我们可以像使用7对所有整数取模那样, 用它对所有多项式取模,
    模它而产生的所有 **余多项式**, 包含所有最高次幂小于2的4个多项式:
    <img src="https://www.zhihu.com/equation?tex=%200%2C%201%2C%20x%2C%20%28x%20%2B%201%29%20" alt=" 0, 1, x, (x + 1) " class="ee_img tr_noresize" eeimg="1">

    这4个多项式就是 GF(2) 在多项式 <img src="https://www.zhihu.com/equation?tex=P_2%28x%29" alt="P_2(x)" class="ee_img tr_noresize" eeimg="1"> 的扩张: 我们把{0, 1} 2个元素的域扩张成
    4个元素的域.

    > 这4个多项式可以表示成4个2bit的二进制数:00,01,10,11


<a class="md-anchor" name="gf2-扩张成-gf28"></a>

### GF(2) 扩张成 GF(2^8)

为了扩张到 <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E8%29%20" alt=" GF(2^8) " class="ee_img tr_noresize" eeimg="1"> 我们选择的8次幂的质多项式是:

<img src="https://www.zhihu.com/equation?tex=P_8%28x%29%20%3D%20x%5E8%20%2B%20x%5E4%20%2B%20x%5E3%20%2B%20x%5E2%20%2B%201%5C%5C" alt="P_8(x) = x^8 + x^4 + x^3 + x^2 + 1\\" class="ee_img tr_noresize" eeimg="1">

这个8次幂的质多项式,模它的所有余多项式,是所有最高次幂不超过7的多项式, 共256个,
它就是 GF(2) 到 GF(256) 的扩张, 扩张后的元素对应0~255这256个二进制数.

因为多项式和二进制数的直接对应关系, <img src="https://www.zhihu.com/equation?tex=%20P_8%28x%29%20" alt=" P_8(x) " class="ee_img tr_noresize" eeimg="1"> 对应:

-   二进制: 1 0001 1101
-   16进制: 0x11d

而GF(256)中的四则运算如下:

-   加法:
    <img src="https://www.zhihu.com/equation?tex=%20a%20%E2%8A%95%20b%20" alt=" a ⊕ b " class="ee_img tr_noresize" eeimg="1"> 对应多项式加法,
    同时它表示的二进制数的加法对应: a ^ b

-   乘法:
    <img src="https://www.zhihu.com/equation?tex=%20a%20%E2%8A%97%20b%20" alt=" a ⊗ b " class="ee_img tr_noresize" eeimg="1"> 对应多项式的乘法(模<img src="https://www.zhihu.com/equation?tex=P_8%28x%29" alt="P_8(x)" class="ee_img tr_noresize" eeimg="1">):

总结一下GF(256)能够满足EC运算的几个性质:

-   加法单位元: 0
-   乘法单位元: 1
-   每个元素对加法都有逆元(可以实现减法): 逆元就是它本身( (x+1) + (x+1) = 0 )
-   每个元素对乘法都有逆元(除了0)(可以实现除法):<img src="https://www.zhihu.com/equation?tex=P_8%28x%29" alt="P_8(x)" class="ee_img tr_noresize" eeimg="1">是不可约的, 因此不存在a和b都不是0但ab=0; 又因为GF(256)只有255个非0元素, 因此对a,总能找到1个x使得 <img src="https://www.zhihu.com/equation?tex=%20a%5Ex%20%3D%20a%20" alt=" a^x = a " class="ee_img tr_noresize" eeimg="1">. 所以 <img src="https://www.zhihu.com/equation?tex=a%5E%7Bx-2%7D%20a%20%3D%201" alt="a^{x-2} a = 1" class="ee_img tr_noresize" eeimg="1"> <img src="https://www.zhihu.com/equation?tex=%20a%5E%7Bx-2%7D%20" alt=" a^{x-2} " class="ee_img tr_noresize" eeimg="1">是a的乘法逆元.
-   乘法和加法满足分配率: 基于多项式乘法和加法的定义.

满足这些性质的四则运算, 就可以用来建立高次曲线, 进而在GF(256)上实现EC.

<a name="#ec-impl"></a>

<a class="md-anchor" name="实现"></a>

# 实现

<a class="md-anchor" name="标准ec的实现"></a>

## 标准EC的实现

以上讨论的是标准的EC的原理, 现在我们将以上的内容总结, 应用到实践上面.

-   四则运算基于 <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E8%29%20" alt=" GF(2^8) " class="ee_img tr_noresize" eeimg="1"> 或 <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E%7B16%7D%29%2C%20GF%282%5E%7B32%7D%29%20" alt=" GF(2^{16}), GF(2^{32}) " class="ee_img tr_noresize" eeimg="1">, 分别对应1字节,
    2字节或4字节.

-   <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E8%29%20" alt=" GF(2^8) " class="ee_img tr_noresize" eeimg="1"> 下的加减法直接用`异或`计算, 不需要其他的工作.

-   <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E8%29%20" alt=" GF(2^8) " class="ee_img tr_noresize" eeimg="1"> 下的乘法和除法用查表的方式实现.

    首先生成 <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E8%29%20" alt=" GF(2^8) " class="ee_img tr_noresize" eeimg="1"> 下对2的指数表和对数表,
    然后把乘除法转换成取对数和取幂的操作:

    以 <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E8%29%20" alt=" GF(2^8) " class="ee_img tr_noresize" eeimg="1"> 为例:

    -   生成指数表 <img src="https://www.zhihu.com/equation?tex=%202%5E0%2C%202%5E1%2C%202%5E2...%20" alt=" 2^0, 2^1, 2^2... " class="ee_img tr_noresize" eeimg="1">的表,
        表中元素 <img src="https://www.zhihu.com/equation?tex=%20p_i%20%3D%202%5Ei%20" alt=" p_i = 2^i " class="ee_img tr_noresize" eeimg="1">.

    -   生成对数表, 表中元素 <img src="https://www.zhihu.com/equation?tex=%20l_i%20%3D%20log_2i%20" alt=" l_i = log_2i " class="ee_img tr_noresize" eeimg="1">.

    生成2个表的代码很简单, 用python表示如下:

    ```python
    power, log = [0] * 256, [0] * 256
    n = 1
    for i in range(0, 256):

        power[i] = n
        log[n] = i

        n *= 2

        # modular by the prime polynomial: P_8(x) = x^8 + x^4 + x^3 + x^2 + 1
        if n >= 256:
            n = n ^ 0x11d

    log[1] = 0 # log[1] is 255, but it should be 0
    ```

    ```
    指数表:
    01 02 04 08 10 20 40 80 1d 3a 74 e8 cd 87 13 26
    4c 98 2d 5a b4 75 ea c9 8f 03 06 0c 18 30 60 c0
    9d 27 4e 9c 25 4a 94 35 6a d4 b5 77 ee c1 9f 23
    46 8c 05 0a 14 28 50 a0 5d ba 69 d2 b9 6f de a1
    5f be 61 c2 99 2f 5e bc 65 ca 89 0f 1e 3c 78 f0
    fd e7 d3 bb 6b d6 b1 7f fe e1 df a3 5b b6 71 e2
    d9 af 43 86 11 22 44 88 0d 1a 34 68 d0 bd 67 ce
    81 1f 3e 7c f8 ed c7 93 3b 76 ec c5 97 33 66 cc
    85 17 2e 5c b8 6d da a9 4f 9e 21 42 84 15 2a 54
    a8 4d 9a 29 52 a4 55 aa 49 92 39 72 e4 d5 b7 73
    e6 d1 bf 63 c6 91 3f 7e fc e5 d7 b3 7b f6 f1 ff
    e3 db ab 4b 96 31 62 c4 95 37 6e dc a5 57 ae 41
    82 19 32 64 c8 8d 07 0e 1c 38 70 e0 dd a7 53 a6
    51 a2 59 b2 79 f2 f9 ef c3 9b 2b 56 ac 45 8a 09
    12 24 48 90 3d 7a f4 f5 f7 f3 fb eb cb 8b 0b 16
    2c 58 b0 7d fa e9 cf 83 1b 36 6c d8 ad 47 8e 01
    ```

    ```
    对数表(0没有以2为底的对数):
    00 00 01 19 02 32 1a c6 03 df 33 ee 1b 68 c7 4b
    04 64 e0 0e 34 8d ef 81 1c c1 69 f8 c8 08 4c 71
    05 8a 65 2f e1 24 0f 21 35 93 8e da f0 12 82 45
    1d b5 c2 7d 6a 27 f9 b9 c9 9a 09 78 4d e4 72 a6
    06 bf 8b 62 66 dd 30 fd e2 98 25 b3 10 91 22 88
    36 d0 94 ce 8f 96 db bd f1 d2 13 5c 83 38 46 40
    1e 42 b6 a3 c3 48 7e 6e 6b 3a 28 54 fa 85 ba 3d
    ca 5e 9b 9f 0a 15 79 2b 4e d4 e5 ac 73 f3 a7 57
    07 70 c0 f7 8c 80 63 0d 67 4a de ed 31 c5 fe 18
    e3 a5 99 77 26 b8 b4 7c 11 44 92 d9 23 20 89 2e
    37 3f d1 5b 95 bc cf cd 90 87 97 b2 dc fc be 61
    f2 56 d3 ab 14 2a 5d 9e 84 3c 39 53 47 6d 41 a2
    1f 2d 43 d8 b7 7b a4 76 c4 17 49 ec 7f 0c 6f f6
    6c a1 3b 52 29 9d 55 aa fb 60 86 b1 bb cc 3e 5a
    cb 59 5f b0 9c a9 a0 51 0b f5 16 eb 7a 75 2c d7
    4f ae d5 e9 e6 e7 ad e8 74 d6 f4 ea a8 50 58 af
    ```

    在计算 <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E8%29%20" alt=" GF(2^8) " class="ee_img tr_noresize" eeimg="1">中的乘法
    将 a, b 通过查对数表和指数表实现:
    <img src="https://www.zhihu.com/equation?tex=%20a%20%5Ctimes%20b%20%3D%202%5E%7Blog_2a%2Blog_2b%7D%20" alt=" a \times b = 2^{log_2a+log_2b} " class="ee_img tr_noresize" eeimg="1">.

    > NOTE:<br/>
    > [Galois-Field](https://en.wikipedia.org/wiki/Finite_field) 的计算目前实现都是基于查表的,
    > 所以选择大的域虽然可以一次计算多个字节,
    > 但内存中随机访问一个大表也可能会造成cache miss太多而影响性能.


    > 一般CPU都没有支持GF乘除法的指令, 但有些专用的硬件卡专门加速GF的乘除法.


-   生成GF后, 选择一个系数矩阵, 常用的是 [Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix) 或 [Cauchy](https://en.wikipedia.org/wiki/Cauchy_matrix).

<a class="md-anchor" name="ec编码-校验数据生成"></a>

### EC编码: 校验数据生成

通常使用1个矩阵来表示输入和输出的关系
(而不是像上文中只使用校验块的生成矩阵),
这里选择自然数生成的 [Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix) 矩阵:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bbmatrix%7D1%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%20%5Cdots%20%20%26%200%20%20%20%20%20%20%20%5C%5C0%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%20%5Cdots%20%20%26%200%20%20%20%20%20%20%20%5C%5C0%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%20%5Cdots%20%20%26%200%20%20%20%20%20%20%20%5C%5C%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cddots%20%26%20%5Cvdots%20%20%5C%5C0%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%20%5Cdots%20%20%26%201%20%20%20%20%20%20%20%5C%5C%5Chline%20%5C%5C1%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%20%5Cdots%20%20%26%201%20%20%20%20%20%20%20%5C%5C1%20%20%20%20%20%20%26%202%20%20%20%20%20%20%26%202%5E2%20%20%20%20%26%20%5Cdots%20%20%26%202%5E%7Bk-1%7D%20%5C%5C1%20%20%20%20%20%20%26%203%20%20%20%20%20%20%26%203%5E2%20%20%20%20%26%20%5Cdots%20%20%26%203%5E%7Bk-1%7D%20%5C%5C%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cddots%20%26%20%5Cvdots%20%20%5C%5C1%20%20%20%20%20%20%26%20m%20%20%20%20%20%20%26%20m%5E2%20%20%20%20%26%20%5Cdots%20%20%26%20m%5E%7Bk-1%7D%5Cend%7Bbmatrix%7D%5Ctimes%5Cbegin%7Bbmatrix%7Dd_1%20%5C%5Cd_2%20%5C%5Cd_3%20%5C%5C...%20%5C%5Cd_k%5Cend%7Bbmatrix%7D%20%3D%5Cbegin%7Bbmatrix%7Dd_1%20%5C%5Cd_2%20%5C%5Cd_3%20%5C%5C...%20%5C%5Cd_k%20%5C%5Cy_1%20%5C%5Cy_2%20%5C%5Cy_3%20%5C%5C...%20%5C%5Cy_m%5Cend%7Bbmatrix%7D%5C%5C" alt="\begin{bmatrix}1      & 0      & 0      & \dots  & 0       \\0      & 1      & 0      & \dots  & 0       \\0      & 0      & 1      & \dots  & 0       \\\vdots & \vdots & \vdots & \ddots & \vdots  \\0      & 0      & 0      & \dots  & 1       \\\hline \\1      & 1      & 1      & \dots  & 1       \\1      & 2      & 2^2    & \dots  & 2^{k-1} \\1      & 3      & 3^2    & \dots  & 3^{k-1} \\\vdots & \vdots & \vdots & \ddots & \vdots  \\1      & m      & m^2    & \dots  & m^{k-1}\end{bmatrix}\times\begin{bmatrix}d_1 \\d_2 \\d_3 \\... \\d_k\end{bmatrix} =\begin{bmatrix}d_1 \\d_2 \\d_3 \\... \\d_k \\y_1 \\y_2 \\y_3 \\... \\y_m\end{bmatrix}\\" class="ee_img tr_noresize" eeimg="1">

这个矩阵里上面是1个大小为`k`的单位矩阵, 表示 <img src="https://www.zhihu.com/equation?tex=%20d_j%20" alt=" d_j " class="ee_img tr_noresize" eeimg="1"> 的输入和输出不变.

下面一部分是1个 <img src="https://www.zhihu.com/equation?tex=%20m%20%5Ctimes%20k%20" alt=" m \times k " class="ee_img tr_noresize" eeimg="1"> 的矩阵表示校验块的计算.

对要存储的k组数据, 逐字节读入, 形成 <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2...d_k%20" alt=" d_1, d_2...d_k " class="ee_img tr_noresize" eeimg="1">, 进行矩阵乘法运算,
得到最后要存储的 k 个数据块和 m 个校验块.

> 之所以把单位矩阵也放到编码矩阵上面, 看起来没有什么用,
> 只是把输入无变化的输出出来的这种风格, 原因在于在编码理论中,
> 并不是所有的生成的Code都是k个原始数据 和 m个校验数据的形式,
> 有些编码算法是将k个输入变成完全不1样的`k+m`个输出, 对这类编码算法,
> 需要1个`k*(k+m)`的编码矩阵来表示全部的转换过程.
> 例如著名的 [Hamming-7-4](https://en.wikipedia.org/wiki/Hamming(7,4)) 编码的编码矩阵(输入k=4, 输出k+m=7):
> 
> <img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D1%261%260%261%5C%5C1%260%261%261%5C%5C1%260%260%260%5C%5C0%261%261%261%5C%5C0%261%260%260%5C%5C0%260%261%260%5C%5C0%260%260%261%5C%5C%5Cend%7Bpmatrix%7D%5C%5C" alt="\begin{pmatrix}1&1&0&1\\1&0&1&1\\1&0&0&0\\0&1&1&1\\0&1&0&0\\0&0&1&0\\0&0&0&1\\\end{pmatrix}\\" class="ee_img tr_noresize" eeimg="1">
> 
> EC中也使用了`k*(k+m)`的编码矩阵.


<a class="md-anchor" name="ec解码"></a>

### EC解码

当数据损坏时, 通过生成解码矩阵来恢复数据:

对所有丢失的数据,
将它对应的第i行从编码矩阵中移除,
移除后, 保留编码矩阵的前k行,
构成1个`k*k`的矩阵.

例如第 2, 3个数据块丢失, 移除第2, 3行, 保留第k+1和k+2行:
这时矩阵, 数据块(没丢失的和丢失的),
没丢失的数据块(<img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_4%2C%20d_5...%20" alt=" d_1, d_4, d_5... " class="ee_img tr_noresize" eeimg="1">),
校验块(<img src="https://www.zhihu.com/equation?tex=%20y_1%2C%20y_2%20" alt=" y_1, y_2 " class="ee_img tr_noresize" eeimg="1">)的关系是:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bbmatrix%7D1%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%20%5Cdots%20%20%26%200%20%20%20%20%20%20%20%5C%5C0%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%20%5Cdots%20%20%26%200%20%20%20%20%20%20%20%5C%5C%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cddots%20%26%20%5Cvdots%20%20%5C%5C0%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%20%5Cdots%20%20%26%201%20%20%20%20%20%20%20%5C%5C1%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%20%5Cdots%20%20%26%201%20%20%20%20%20%20%20%5C%5C1%20%20%20%20%20%20%26%202%20%20%20%20%20%20%26%202%5E2%20%20%20%20%26%202%5E3%20%20%20%20%26%20%5Cdots%20%20%26%202%5E%7Bk-1%7D%20%5C%5C%5Cend%7Bbmatrix%7D%5Ctimes%5Cbegin%7Bbmatrix%7Dd_1%20%5C%5Cu_2%20%5C%5Cu_3%20%5C%5Cd_4%20%5C%5C...%20%5C%5Cd_k%5Cend%7Bbmatrix%7D%20%3D%5Cbegin%7Bbmatrix%7Dd_1%20%5C%5Cd_4%20%5C%5C...%20%5C%5Cd_k%20%5C%5Cy_1%20%5C%5Cy_2%20%5C%5C%5Cend%7Bbmatrix%7D%5C%5C" alt="\begin{bmatrix}1      & 0      & 0      & 0      & \dots  & 0       \\0      & 0      & 0      & 1      & \dots  & 0       \\\vdots & \vdots & \vdots & \vdots & \ddots & \vdots  \\0      & 0      & 0      & 0      & \dots  & 1       \\1      & 1      & 1      & 1      & \dots  & 1       \\1      & 2      & 2^2    & 2^3    & \dots  & 2^{k-1} \\\end{bmatrix}\times\begin{bmatrix}d_1 \\u_2 \\u_3 \\d_4 \\... \\d_k\end{bmatrix} =\begin{bmatrix}d_1 \\d_4 \\... \\d_k \\y_1 \\y_2 \\\end{bmatrix}\\" class="ee_img tr_noresize" eeimg="1">

最后求逆矩阵, 和没有丢失的块相乘, 就可以恢复出丢失的数据块 <img src="https://www.zhihu.com/equation?tex=%20u_2%2C%20u_3%20" alt=" u_2, u_3 " class="ee_img tr_noresize" eeimg="1">:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bbmatrix%7Dd_1%20%5C%5Cu_2%20%5C%5Cu_3%20%5C%5Cd_4%20%5C%5C...%20%5C%5Cd_k%5Cend%7Bbmatrix%7D%20%3D%5Cbegin%7Bbmatrix%7D1%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%20%5Cdots%20%20%26%200%20%20%20%20%20%20%20%5C%5C0%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%20%5Cdots%20%20%26%200%20%20%20%20%20%20%20%5C%5C%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cvdots%20%26%20%5Cddots%20%26%20%5Cvdots%20%20%5C%5C0%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%20%5Cdots%20%20%26%201%20%20%20%20%20%20%20%5C%5C1%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%20%5Cdots%20%20%26%201%20%20%20%20%20%20%20%5C%5C1%20%20%20%20%20%20%26%202%20%20%20%20%20%20%26%202%5E2%20%20%20%20%26%202%5E3%20%20%20%20%26%20%5Cdots%20%20%26%202%5E%7Bk-1%7D%20%5C%5C%5Cend%7Bbmatrix%7D%5E%7B-1%7D%5Ctimes%5Cbegin%7Bbmatrix%7Dd_1%20%5C%5Cd_4%20%5C%5C...%20%5C%5Cd_k%20%5C%5Cy_1%20%5C%5Cy_2%20%5C%5C%5Cend%7Bbmatrix%7D%5C%5C" alt="\begin{bmatrix}d_1 \\u_2 \\u_3 \\d_4 \\... \\d_k\end{bmatrix} =\begin{bmatrix}1      & 0      & 0      & 0      & \dots  & 0       \\0      & 0      & 0      & 1      & \dots  & 0       \\\vdots & \vdots & \vdots & \vdots & \ddots & \vdots  \\0      & 0      & 0      & 0      & \dots  & 1       \\1      & 1      & 1      & 1      & \dots  & 1       \\1      & 2      & 2^2    & 2^3    & \dots  & 2^{k-1} \\\end{bmatrix}^{-1}\times\begin{bmatrix}d_1 \\d_4 \\... \\d_k \\y_1 \\y_2 \\\end{bmatrix}\\" class="ee_img tr_noresize" eeimg="1">

因为只有 <img src="https://www.zhihu.com/equation?tex=%20u_2%2C%20u_3%20" alt=" u_2, u_3 " class="ee_img tr_noresize" eeimg="1"> 丢失了, 矩阵相乘时只需要计算逆矩阵的第2, 3行.

<a class="md-anchor" name="vandermonde-矩阵的可逆性"></a>

### Vandermonde 矩阵的可逆性

实数下的Vandermonde 矩阵是一定可逆的, 但它的任意n行n列组成的子矩阵**不一定**是可逆的.

假设一个 Vandermonde 矩阵, 如果存在一个 $ [ a_1, a_2, a_3 ] $, 使得乘积为全0,
则矩阵n列是线性相关的:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bbmatrix%7D1%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%201%20%20%20%20%20%5C%5C1%20%20%20%20%20%20%26%20x_1%20%20%20%20%26%20x_1%5E2%20%5C%5C1%20%20%20%20%20%20%26%20x_2%20%20%20%20%26%20x_2%5E2%20%5C%5C%5Cend%7Bbmatrix%7D%5Ctimes%5Cbegin%7Bbmatrix%7Da_1%20%5C%5Ca_2%20%5C%5Ca_3%20%5C%5C%5Cend%7Bbmatrix%7D%20%3D%5Cbegin%7Bbmatrix%7D0%20%5C%5C0%20%5C%5C0%20%5C%5C%5Cend%7Bbmatrix%7D%5C%5C" alt="\begin{bmatrix}1      & 1      & 1     \\1      & x_1    & x_1^2 \\1      & x_2    & x_2^2 \\\end{bmatrix}\times\begin{bmatrix}a_1 \\a_2 \\a_3 \\\end{bmatrix} =\begin{bmatrix}0 \\0 \\0 \\\end{bmatrix}\\" class="ee_img tr_noresize" eeimg="1">

因为方程:
<img src="https://www.zhihu.com/equation?tex=%20a_1%20%2B%20a_2%20x%20%2B%20a_3%20x%5E2%20%3D%200%20" alt=" a_1 + a_2 x + a_3 x^2 = 0 " class="ee_img tr_noresize" eeimg="1">
最多只有2个解, 但原矩阵 要求有3个不同的值 <img src="https://www.zhihu.com/equation?tex=%201%2C%20x_1%2C%20x_2%20" alt=" 1, x_1, x_2 " class="ee_img tr_noresize" eeimg="1"> 满足这个方程.
因此不存在这一的 <img src="https://www.zhihu.com/equation?tex=%20a_i%20" alt=" a_i " class="ee_img tr_noresize" eeimg="1"> 使得 Vandermonde 矩阵线性相关.

但如果查看一个 Vandermonde 矩阵的子矩阵(<img src="https://www.zhihu.com/equation?tex=%200%20%3C%20u%20%3C%20v%20" alt=" 0 < u < v " class="ee_img tr_noresize" eeimg="1">):

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bbmatrix%7D1%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%201%20%20%20%20%20%5C%5C1%20%20%20%20%20%20%26%20x_1%5Eu%20%20%26%20x_1%5Ev%20%5C%5C1%20%20%20%20%20%20%26%20x_2%5Eu%20%20%26%20x_2%5Ev%20%5C%5C%5Cend%7Bbmatrix%7D%5Ctimes%5Cbegin%7Bbmatrix%7Da_1%20%5C%5Ca_2%20%5C%5Ca_3%20%5C%5C%5Cend%7Bbmatrix%7D%20%3D%5Cbegin%7Bbmatrix%7D0%20%5C%5C0%20%5C%5C0%20%5C%5C%5Cend%7Bbmatrix%7D%5C%5C" alt="\begin{bmatrix}1      & 1      & 1     \\1      & x_1^u  & x_1^v \\1      & x_2^u  & x_2^v \\\end{bmatrix}\times\begin{bmatrix}a_1 \\a_2 \\a_3 \\\end{bmatrix} =\begin{bmatrix}0 \\0 \\0 \\\end{bmatrix}\\" class="ee_img tr_noresize" eeimg="1">

因为方程:
<img src="https://www.zhihu.com/equation?tex=%20a_1%20%2B%20a_2%20x%5Eu%20%2B%20a_3%20x%5Ev%20%3D%200%20" alt=" a_1 + a_2 x^u + a_3 x^v = 0 " class="ee_img tr_noresize" eeimg="1">
最多有v个解, 只要v 大于2, 就可能找到一组 <img src="https://www.zhihu.com/equation?tex=%20a_i%20" alt=" a_i " class="ee_img tr_noresize" eeimg="1"> 和 <img src="https://www.zhihu.com/equation?tex=%20x_i%20" alt=" x_i " class="ee_img tr_noresize" eeimg="1">, 使得上面的子矩阵线性相关.

例如, 一个子矩阵, x=-1 时, 矩阵不可逆:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bbmatrix%7D1%20%20%20%20%20%20%26%201%20%20%20%20%5C%5C1%20%20%20%20%20%20%26%20x%5E2%20%20%5C%5C%5Cend%7Bbmatrix%7D%5C%5C" alt="\begin{bmatrix}1      & 1    \\1      & x^2  \\\end{bmatrix}\\" class="ee_img tr_noresize" eeimg="1">

<a class="md-anchor" name="gf256-下的-vandermonde-矩阵的可逆性"></a>

### GF256 下的 Vandermonde 矩阵的可逆性

在 <img src="https://www.zhihu.com/equation?tex=%20GF%282%5E8%29%20" alt=" GF(2^8) " class="ee_img tr_noresize" eeimg="1"> 下的 Vandermonde 矩阵, 除了上面的的不可逆情况外,
还有另外一种情况导致子矩阵不可逆.

举例来说, 以下矩阵是缺失 <img src="https://www.zhihu.com/equation?tex=%20u_1%2C%20u_4%20" alt=" u_1, u_4 " class="ee_img tr_noresize" eeimg="1"> 情况下的用来恢复数据的矩阵,
它可能不可逆: 如果 <img src="https://www.zhihu.com/equation?tex=%20x%5E3%20%3D%3D%201%20" alt=" x^3 == 1 " class="ee_img tr_noresize" eeimg="1">,

由于2是1个生成元,  容易看出, <img src="https://www.zhihu.com/equation?tex=%20x%20%3D%202%5E%7B85%7D%20" alt=" x = 2^{85} " class="ee_img tr_noresize" eeimg="1"> 是1个不可逆的情况:
<img src="https://www.zhihu.com/equation?tex=%20x%5E3%20%3D%201%20" alt=" x^3 = 1 " class="ee_img tr_noresize" eeimg="1"> 于是第1列和第4列完全一样.

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bbmatrix%7D0%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%5C%5C0%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%5C%5C0%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%200%20%20%20%20%20%20%26%201%20%20%20%5C%5C1%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%201%20%20%20%20%20%20%26%201%20%20%20%5C%5C1%20%20%20%20%20%20%26%20x%20%20%20%20%20%20%26%20x%5E2%20%20%20%20%26%20x%5E3%20%20%20%20%26%20x%5E4%20%5C%5C%5Cend%7Bbmatrix%7D%5C%5C" alt="\begin{bmatrix}0      & 1      & 0      & 0      & 0   \\0      & 0      & 1      & 0      & 0   \\0      & 0      & 0      & 0      & 1   \\1      & 1      & 1      & 1      & 1   \\1      & x      & x^2    & x^3    & x^4 \\\end{bmatrix}\\" class="ee_img tr_noresize" eeimg="1">

> Cauchy 矩阵的任意n行n列组成的矩阵都是可逆的, 因为任意子矩阵还是 Cauchy矩阵.


<a class="md-anchor" name="数据恢复io优化-lrc-local-reconstruction-code"></a>

## 数据恢复IO优化: LRC: 
[Local-Reconstruction-Code]

当 EC 进行数据恢复的时候, 需要k个块参与数据恢复, 直观上,
每个数据块损坏都需要k倍的IO消耗.

为了缓解这个问题, 一种略微提高冗余度, 但可以大大降低恢复IO的算法被提出:
[Local-Reconstruction-Code], 简称 LRC.

LRC的思路很简单, 在原来的 EC 的基础上,
对所有的数据块分组对每组在做1次 <img src="https://www.zhihu.com/equation?tex=%20k%27%20%2B%201%20" alt=" k' + 1 " class="ee_img tr_noresize" eeimg="1"> 的 EC.
k' 是二次分组的每组的数据块的数量.

<a class="md-anchor" name="lrc-的校验块生成"></a>

### LRC 的校验块生成

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Baligned%7D%5Coverbrace%7Bd_1%20%2B%20d_2%20%2B%20d_3%7D%5E%7By_%7B1%2C1%7D%7D%20%2B%20%5Coverbrace%7Bd_4%20%2B%20d_5%20%2B%20d_6%7D%5E%7By_%7B1%2C2%7D%7D%20%26%20%3D%20y_1%20%5C%5Cd_1%20%2B%202d_2%20%2B%202%5E2d_3%20%2B%202%5E3d_4%20%2B%202%5E4d_5%20%2B%202%5E5d_6%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%26%20%3D%20y_2%20%5C%5Cd_1%20%2B%203d_2%20%2B%203%5E2d_3%20%2B%203%5E3d_4%20%2B%203%5E4d_5%20%2B%203%5E5d_6%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%26%20%3D%20y_3%5Cend%7Baligned%7D%5C%5C" alt="\begin{aligned}\overbrace{d_1 + d_2 + d_3}^{y_{1,1}} + \overbrace{d_4 + d_5 + d_6}^{y_{1,2}} & = y_1 \\d_1 + 2d_2 + 2^2d_3 + 2^3d_4 + 2^4d_5 + 2^5d_6                                & = y_2 \\d_1 + 3d_2 + 3^2d_3 + 3^3d_4 + 3^4d_5 + 3^5d_6                                & = y_3\end{aligned}\\" class="ee_img tr_noresize" eeimg="1">

最终保存的块是所有的数据块: <img src="https://www.zhihu.com/equation?tex=%20d_1%2C%20d_2%2C%20d_3%2C%20d_4%2C%20d_5%2C%20d_6%20" alt=" d_1, d_2, d_3, d_4, d_5, d_6 " class="ee_img tr_noresize" eeimg="1">,
和校验块 <img src="https://www.zhihu.com/equation?tex=%20y_%7B1%2C1%7D%2C%20y_%7B1%2C2%7D%2C%20y_2%2C%20y_3%20" alt=" y_{1,1}, y_{1,2}, y_2, y_3 " class="ee_img tr_noresize" eeimg="1">.

这里不需要保存 <img src="https://www.zhihu.com/equation?tex=%20y_1%20" alt=" y_1 " class="ee_img tr_noresize" eeimg="1"> 因为 <img src="https://www.zhihu.com/equation?tex=%20y_1%20%3D%20y_%7B1%2C1%7D%20%2B%20y_%7B1%2C2%7D%20" alt=" y_1 = y_{1,1} + y_{1,2} " class="ee_img tr_noresize" eeimg="1">

对于 LRC的EC来说, 它的生成矩阵前k行不变,
去掉了标准EC的第k+1行, 多出2个局部的校验行:

<img src="https://www.zhihu.com/equation?tex=%5Cbegin%7Bbmatrix%7D1%20%26%200%20%26%200%20%26%200%20%26%200%20%26%200%20%5C%5C0%20%26%201%20%26%200%20%26%200%20%26%200%20%26%200%20%5C%5C0%20%26%200%20%26%201%20%26%200%20%26%200%20%26%200%20%5C%5C0%20%26%200%20%26%200%20%26%201%20%26%200%20%26%200%20%5C%5C0%20%26%200%20%26%200%20%26%200%20%26%201%20%26%200%20%5C%5C0%20%26%200%20%26%200%20%26%200%20%26%200%20%26%201%20%5C%5C%5Chline%20%5C%5C1%20%26%201%20%26%201%20%26%200%20%26%200%20%26%200%20%5C%5C0%20%26%200%20%26%200%20%26%201%20%26%201%20%26%201%20%5C%5C%5Chline%20%5C%5C1%20%26%202%20%26%202%5E2%20%26%202%5E3%20%26%202%5E4%20%26%202%5E5%20%5C%5C1%20%26%203%20%26%203%5E2%20%26%203%5E3%20%26%203%5E4%20%26%203%5E5%20%5C%5C%5Cend%7Bbmatrix%7D%5Ctimes%5Cbegin%7Bbmatrix%7Dd_1%20%5C%5Cd_2%20%5C%5Cd_3%20%5C%5Cd_4%20%5C%5Cd_5%20%5C%5Cd_6%5Cend%7Bbmatrix%7D%20%3D%5Cbegin%7Bbmatrix%7Dd_1%20%5C%5Cd_2%20%5C%5Cd_3%20%5C%5Cd_4%20%5C%5Cd_5%20%5C%5Cd_6%20%5C%5Cy_%7B1%2C1%7D%20%5C%5Cy_%7B1%2C2%7D%20%5C%5Cy_2%20%5C%5Cy_3%20%5C%5C%5Cend%7Bbmatrix%7D%5C%5C" alt="\begin{bmatrix}1 & 0 & 0 & 0 & 0 & 0 \\0 & 1 & 0 & 0 & 0 & 0 \\0 & 0 & 1 & 0 & 0 & 0 \\0 & 0 & 0 & 1 & 0 & 0 \\0 & 0 & 0 & 0 & 1 & 0 \\0 & 0 & 0 & 0 & 0 & 1 \\\hline \\1 & 1 & 1 & 0 & 0 & 0 \\0 & 0 & 0 & 1 & 1 & 1 \\\hline \\1 & 2 & 2^2 & 2^3 & 2^4 & 2^5 \\1 & 3 & 3^2 & 3^3 & 3^4 & 3^5 \\\end{bmatrix}\times\begin{bmatrix}d_1 \\d_2 \\d_3 \\d_4 \\d_5 \\d_6\end{bmatrix} =\begin{bmatrix}d_1 \\d_2 \\d_3 \\d_4 \\d_5 \\d_6 \\y_{1,1} \\y_{1,2} \\y_2 \\y_3 \\\end{bmatrix}\\" class="ee_img tr_noresize" eeimg="1">

<a class="md-anchor" name="lrc-的数据恢复"></a>

### LRC 的数据恢复

LRC 的数据恢复和标准的EC类似, 除了2点不同:

-   在选择校验块的行生成解码矩阵的时候,
    如果某第k+i行没有覆盖到任何损坏的数据的话,
    是无法提供有效性信息, 需要跳过的.

    例如 <img src="https://www.zhihu.com/equation?tex=%20d_4%20" alt=" d_4 " class="ee_img tr_noresize" eeimg="1"> 损坏时, 不能像标准EC那样选择第7行 `1 1 1 0 0 0`
    这行作为补充的校验行生成解码矩阵, 必须略过第7行, 使用第8行.

-   不是所有的情况下, m个数据损坏都可以通过加入m个校验行来恢复.
    因为LRC的生成矩阵没有遵循 [Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix) 矩阵的规则,
    不能保证任意k行都是满秩的.

<a name="ec-analysis"></a>

<a class="md-anchor" name="工程优化"></a>

## 工程优化

插播一条广告:
徐同学的博客中给出了很好的EC工程实现的介绍,
推荐!: [实现高性能纠删码引擎](http://www.templex.xyz/blog/101/writers.html)

<a class="md-anchor" name="分析"></a>

# 分析

<a class="md-anchor" name="可靠性分析"></a>

## 可靠性分析

在可靠性方面, 假设 EC 的配置是k个数据块, m个校验块.
根据 EC 的定义,k+m个块中, 任意丢失m个都可以将其找回.
这个 EC 组的丢失数据的风险就是丢失m+1个块或更多的风险:

<img src="https://www.zhihu.com/equation?tex=%5Csum_%7Bi%3Dm%2B1%7D%5E%7Bk%2Bm%7D%20%7Bk%2Bm%20%5Cchoose%20i%7D%20p%5E%7Bi%7D%20%281-p%29%5E%7Bk%2Bm-i%7D%5C%5C" alt="\sum_{i=m+1}^{k+m} {k+m \choose i} p^{i} (1-p)^{k+m-i}\\" class="ee_img tr_noresize" eeimg="1">

这里p是单块数据丢失的风险,一般选择磁盘的日损坏率: 大约是`0.0001`.
p一般很小所以近似就只看第1项:

<img src="https://www.zhihu.com/equation?tex=%7Bk%2Bm%20%5Cchoose%20m%2B1%7D%20p%5E%7Bm%2B1%7D%20%281-p%29%5E%7Bk-1%7D%5C%5C" alt="{k+m \choose m+1} p^{m+1} (1-p)^{k-1}\\" class="ee_img tr_noresize" eeimg="1">

2个校验块和3副本的可靠性对比(取m=2):

<table>
<tr class="header">
<th style="text-align: left;">k</th>
<th style="text-align: left;">m</th>
<th style="text-align: left;">丢数据风险</th>
</tr>
<tr class="odd">
<td style="text-align: left;">1</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;"><br /><span class="math display">1 × 10<sup> − 12</sup></span><br /> (1个数据块+2个校验块 可靠性 和 3副本等价)</td>
</tr>
<tr class="even">
<td style="text-align: left;">2</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;"><br /><span class="math display">3 × 10<sup> − 12</sup></span><br /></td>
</tr>
<tr class="odd">
<td style="text-align: left;">3</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;"><br /><span class="math display">9 × 10<sup> − 12</sup></span><br /></td>
</tr>
<tr class="even">
<td style="text-align: left;">10</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;"><br /><span class="math display">2 × 10<sup> − 10</sup></span><br /> (10+2 和 12盘服务器的 <a href="https://zh.wikipedia.org/wiki/RAID#RAID_6">RAID-6</a> 等价)</td>
</tr>
<tr class="odd">
<td style="text-align: left;">32</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;"><br /><span class="math display">5 × 10<sup> − 9</sup></span><br /></td>
</tr>
<tr class="even">
<td style="text-align: left;">64</td>
<td style="text-align: left;">2</td>
<td style="text-align: left;"><br /><span class="math display">4 × 10<sup> − 8</sup></span><br /></td>
</tr>
</table>

3个校验块和4副本的可靠性对比(取m=3):

<table>
<tr class="header">
<th style="text-align: left;">k</th>
<th style="text-align: left;">m</th>
<th style="text-align: left;">丢数据风险</th>
</tr>
<tr class="odd">
<td style="text-align: left;">1</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;"><br /><span class="math display">1 × 10<sup> − 16</sup></span><br /> (1个数据块+3个校验块 可靠性 和 4副本等价)</td>
</tr>
<tr class="even">
<td style="text-align: left;">2</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;"><br /><span class="math display">5 × 10<sup> − 16</sup></span><br /></td>
</tr>
<tr class="odd">
<td style="text-align: left;">3</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;"><br /><span class="math display">2 × 10<sup> − 15</sup></span><br /></td>
</tr>
<tr class="even">
<td style="text-align: left;">10</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;"><br /><span class="math display">7 × 10<sup> − 14</sup></span><br /></td>
</tr>
<tr class="odd">
<td style="text-align: left;">32</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;"><br /><span class="math display">5 × 10<sup> − 12</sup></span><br /></td>
</tr>
<tr class="even">
<td style="text-align: left;">64</td>
<td style="text-align: left;">3</td>
<td style="text-align: left;"><br /><span class="math display">7 × 10<sup> − 11</sup></span><br /></td>
</tr>
</table>

4个校验块和5副本的可靠性对比(取m=4):

<table>
<tr class="header">
<th style="text-align: left;">k</th>
<th style="text-align: left;">m</th>
<th style="text-align: left;">丢数据风险</th>
</tr>
<tr class="odd">
<td style="text-align: left;">1</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;"><br /><span class="math display">1 × 10<sup> − 20</sup></span><br /> (1个数据块+4个校验块 可靠性 和 5副本等价)</td>
</tr>
<tr class="even">
<td style="text-align: left;">2</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;"><br /><span class="math display">6 × 10<sup> − 20</sup></span><br /></td>
</tr>
<tr class="odd">
<td style="text-align: left;">3</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;"><br /><span class="math display">2 × 10<sup> − 19</sup></span><br /></td>
</tr>
<tr class="even">
<td style="text-align: left;">10</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;"><br /><span class="math display">2 × 10<sup> − 17</sup></span><br /></td>
</tr>
<tr class="odd">
<td style="text-align: left;">32</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;"><br /><span class="math display">4 × 10<sup> − 15</sup></span><br /></td>
</tr>
<tr class="even">
<td style="text-align: left;">64</td>
<td style="text-align: left;">4</td>
<td style="text-align: left;"><br /><span class="math display">1 × 10<sup> − 13</sup></span><br /></td>
</tr>
</table>

<a class="md-anchor" name="io消耗"></a>

## IO消耗

以一个 EC 组来分析,
1个块损坏的概率是 <img src="https://www.zhihu.com/equation?tex=%20p%20" alt=" p " class="ee_img tr_noresize" eeimg="1">, 这个组中有块损坏的概率是:
<img src="https://www.zhihu.com/equation?tex=%201%20-%20%281-p%29%5E%7Bk%2Bm%7D%20%5Capprox%20%28k%2Bm%29p%20" alt=" 1 - (1-p)^{k+m} \approx (k+m)p " class="ee_img tr_noresize" eeimg="1">

每次数据损坏都需要读取全组的数据进行恢复.
不论1块损坏还是多块损坏, 数据恢复都是读取1次, 输出1或多次.
恢复数据的输出比较小, 1般是1, 所以可以忽略.

每存储一个字节一天数据恢复产生的传输量是(blocksize是一个数据块或校验块的大小):

<img src="https://www.zhihu.com/equation?tex=%5Cfrac%7B%28k%2Bm%29p%20%5Ctimes%20%28k%2Bm%29%20%5Ctimes%20blocksize%7D%7B%28k%2Bm%29%20%5Ctimes%20blocksize%7D%20%3D%20%28k%2Bm%29p%5C%5C" alt="\frac{(k+m)p \times (k+m) \times blocksize}{(k+m) \times blocksize} = (k+m)p\\" class="ee_img tr_noresize" eeimg="1">

也就是说, 使用 EC 每存储`1TB`的数据,
每天(因为我们取的数据损坏概率是按天计算的)用于数据恢复而产生的IO是
`k * 0.1GB / TB`

磁盘的IO大致上也等同于网络流量, 因为大部分实现必须将数据分布到不同的服务器上.

> NOTE:<br/>
> 随着 `k`的增加, 整体成本虽然会下降(`1+m/k`),
> 但数据恢复的IO开销也会随着k(近似于)线性的增长.


例如:

假设`k+m = 12`:

如果整个集群有 `100PB` 数据,
每天用于恢复数据的网络传输是 `100TB`.

假设单台存储服务器的容量是`30TB`,
每台服务器每天用于数据恢复的数据输出量是 `30GB`,
如果数据恢复能平均到每天的每1秒, 最低的带宽消耗是:
`30GB / 86400 sec/day = 3.0Mbps`.

但一般来说数据恢复不会在时间上很均匀的分布,
这个带宽消耗需要预估10倍到100倍.

---

<a class="md-anchor" name="参考"></a>

# 参考

-   [Vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix)
-   [范德蒙矩阵](https://en.wikipedia.org/wiki/Vandermonde_matrix)
-   [Cauchy](https://en.wikipedia.org/wiki/Cauchy_matrix)
-   [RAID-5](https://zh.wikipedia.org/wiki/RAID#RAID_5)
-   [RAID-6](https://zh.wikipedia.org/wiki/RAID#RAID_6)
-   [Finite-Field](https://en.wikipedia.org/wiki/Finite_field)
-   [Galois-Field](https://en.wikipedia.org/wiki/Finite_field)
-   [伽罗华域](https://en.wikipedia.org/wiki/Finite_field)
-   [Reed-Solomon](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction)
-   [里德-所罗门码](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction)
-   [Erasure-Code](https://en.wikipedia.org/wiki/Erasure_code)
-   [Prime-Polynomial](https://en.wikipedia.org/wiki/Irreducible_polynomial)
-   [Field-Extension](https://en.wikipedia.org/wiki/Field_extension)
-   [Complex-Number](https://en.wikipedia.org/wiki/Irreducible_polynomial#Field_extension)
-   [Hamming-7-4](https://en.wikipedia.org/wiki/Hamming(7,4))
-   [Generator-Matrix](https://en.wikipedia.org/wiki/Generator_matrix)

---

-   [实现高性能纠删码引擎](http://www.templex.xyz/blog/101/writers.html)

---



Reference:

- Cauchy matrix : [https://en.wikipedia.org/wiki/Cauchy_matrix](https://en.wikipedia.org/wiki/Cauchy_matrix)

- Complex-Number : [https://en.wikipedia.org/wiki/Irreducible_polynomial#Field_extension](https://en.wikipedia.org/wiki/Irreducible_polynomial#Field_extension)

- Erasure-Code : [https://en.wikipedia.org/wiki/Erasure_code](https://en.wikipedia.org/wiki/Erasure_code)

- Field-Extension : [https://en.wikipedia.org/wiki/Field_extension](https://en.wikipedia.org/wiki/Field_extension)

- Finite-Field : [https://en.wikipedia.org/wiki/Finite_field](https://en.wikipedia.org/wiki/Finite_field)

- Galois-Field : [https://en.wikipedia.org/wiki/Finite_field](https://en.wikipedia.org/wiki/Finite_field)

- Generator-Matrix : [https://en.wikipedia.org/wiki/Generator_matrix](https://en.wikipedia.org/wiki/Generator_matrix)

- Hamming(7, 4) : [https://en.wikipedia.org/wiki/Hamming(7,4)](https://en.wikipedia.org/wiki/Hamming(7,4))

- Prime-Polynomial : [https://en.wikipedia.org/wiki/Irreducible_polynomial](https://en.wikipedia.org/wiki/Irreducible_polynomial)

- RAID-5 : [https://zh.wikipedia.org/wiki/RAID#RAID_5](https://zh.wikipedia.org/wiki/RAID#RAID_5)

- RAID-6 : [https://zh.wikipedia.org/wiki/RAID#RAID_6](https://zh.wikipedia.org/wiki/RAID#RAID_6)

- Reed-Solomon error correction : [https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction)

- Vandermonde matrix : [https://en.wikipedia.org/wiki/Vandermonde_matrix](https://en.wikipedia.org/wiki/Vandermonde_matrix)

- HDD Failure Rate : [https://www.backblaze.com/blog/hard-drive-reliability-stats-q1-2016/](https://www.backblaze.com/blog/hard-drive-reliability-stats-q1-2016/)


[Cauchy]:            https://en.wikipedia.org/wiki/Cauchy_matrix                          "Cauchy matrix"
[Complex-Number]:    https://en.wikipedia.org/wiki/Irreducible_polynomial#Field_extension "Complex-Number"
[Erasure-Code]:      https://en.wikipedia.org/wiki/Erasure_code                           "Erasure-Code"
[Field-Extension]:   https://en.wikipedia.org/wiki/Field_extension                        "Field-Extension"
[Finite-Field]:      https://en.wikipedia.org/wiki/Finite_field                           "Finite-Field"
[Galois-Field]:      https://en.wikipedia.org/wiki/Finite_field                           "Galois-Field"
[Generator-Matrix]:  https://en.wikipedia.org/wiki/Generator_matrix                       "Generator-Matrix"
[Hamming-7-4]:       https://en.wikipedia.org/wiki/Hamming(7,4)                           "Hamming(7, 4)"
[Prime-Polynomial]:  https://en.wikipedia.org/wiki/Irreducible_polynomial                 "Prime-Polynomial"
[RAID-5]:            https://zh.wikipedia.org/wiki/RAID#RAID_5                            "RAID-5"
[RAID-6]:            https://zh.wikipedia.org/wiki/RAID#RAID_6                            "RAID-6"
[Reed-Solomon]:      https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction  "Reed-Solomon error correction"
[Vandermonde]:       https://en.wikipedia.org/wiki/Vandermonde_matrix                     "Vandermonde matrix"
[failure-rate]:      https://www.backblaze.com/blog/hard-drive-reliability-stats-q1-2016/ "HDD Failure Rate"