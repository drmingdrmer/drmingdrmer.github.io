
文字版: [Erasure-Code: 工作原理, 数学解释, 实践和分析]({% post_url 2017-02-01-ec %})

<!--more-->

![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-00.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-01.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-02.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-03.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-04.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-05.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-06.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-07.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-08.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-09.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-10.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-11.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-12.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-13.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-14.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-15.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-16.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-17.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-18.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-19.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-20.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-21.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-22.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-23.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-24.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-25.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-26.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-27.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-28.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-29.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-30.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-31.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-32.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-33.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-34.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-35.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-36.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-37.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-38.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@_md2zhihu/asset/ec-img/s-ec-39.jpg)

---

文字版: [Erasure-Code: 工作原理, 数学解释, 实践和分析]({% post_url 2017-02-01-ec %})



Reference:

