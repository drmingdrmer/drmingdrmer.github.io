
文字版: [Erasure-Code: 工作原理, 数学解释, 实践和分析]({% post_url 2017-02-01-ec %})

<!--more-->

![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/6a4b3c16c8661cc4-s-ec-00.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/b727762d8bc0c831-s-ec-01.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/82aeebb3b561e19d-s-ec-02.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/42e52d6de07a6d25-s-ec-03.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/9efdc82e1c0042ea-s-ec-04.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/91931651d4f50c94-s-ec-05.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/0a83feeab8971c77-s-ec-06.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/85136cb9cbe4f3e6-s-ec-07.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/f452765e2a785fe3-s-ec-08.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/e97b2af2d06951db-s-ec-09.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/6826142174bbd416-s-ec-10.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/02596484f5dd9a47-s-ec-11.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/441ab1e5acb67932-s-ec-12.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/20a1ee3fd338a1d6-s-ec-13.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/710c5b08ab68c887-s-ec-14.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/be74ae5a6a52d121-s-ec-15.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/9d03d74706a1578e-s-ec-16.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/15fc9797a862f903-s-ec-17.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/3141dae5777a0482-s-ec-18.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/cb6408f1773e9bd0-s-ec-19.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/ae83029fb5d8600f-s-ec-20.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/02ee9fbd52ca265a-s-ec-21.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/711fb43a7678c5aa-s-ec-22.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/7648bdbf141ba097-s-ec-23.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/a34075ad04ff83b8-s-ec-24.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/c7df45c60870120b-s-ec-25.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/b82cc2e61b6950e0-s-ec-26.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/e8f632db1281559b-s-ec-27.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/547ed2c85ade81d6-s-ec-28.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/3f18d6473153c2f6-s-ec-29.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/3e30ae7823f5f73b-s-ec-30.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/6286864b9a426a91-s-ec-31.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/f31da6d611e0172f-s-ec-32.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/cf5e92205299bf0f-s-ec-33.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/428a149a9d882fc1-s-ec-34.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/fe45be354fe260dc-s-ec-35.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/869dfde398b018b6-s-ec-36.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/6194db95328d3188-s-ec-37.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/9dbb441c8a32a2b7-s-ec-38.jpg)
![](https://cdn.jsdelivr.net/gh/drmingdrmer/drmingdrmer.github.io@master-md2zhihu-asset/ec-img/154c6c356c077c51-s-ec-39.jpg)

---

文字版: [Erasure-Code: 工作原理, 数学解释, 实践和分析]({% post_url 2017-02-01-ec %})



Reference:

