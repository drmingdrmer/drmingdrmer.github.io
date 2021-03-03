
<!--excerpt-->

一年前, 一个偶然的机会参加了公司组织的一个成人绘画启蒙班,
突然之间想起一直都想要认真的画画,
从自己跟桌子差不多高的时候, 就喜欢画画.
无奈家长眼中自己的文化课学好了可能更不容易饿死,
于是一直没有什么机会.

这次启蒙班课程其实只有4节左右, 很快就过去了.
但从那时起, 觉得应该把这件事从人生TODOlist里开始去掉了.
于是从2018.10月开始间歇的练练,
俗话说, 一个好汉三个帮, 身边几个好友给了不少帮助.
感谢彪哥淼姐丁老, 加班之余还不忘对我指点12.
俗话又说, 一日为师, 二日为师, 日日日为师.
几个老师也被我折磨的够呛.
可以说, 对我自己的人生产生了关键的影响.

到此为止, 回头看看这一年的变化,
有些进步, 也参差不齐的摸索.
相比外在的变化带来的快乐, 看到自己自身的变化(积极的), 更能让人开心.

<style>
.xp-draw-title {
    display: none;
}
.xp-draw-date {
    display: none;
}
.xp-draw-container {
    display: inline-block;
    width: 10%;
    margin-bottom: 0px;
}
</style>

{% for d in page.drawings %}

<div class="xp-draw-container">
    <div class="xp-draw-title" style="font-size: 1.2rem; line-height: 120%;">{{ d.title }}</div>
    <div class="xp-draw-date" style="font-size: 1.0rem; line-height: 120%;">{{ d.date }}</div>
    <a href="{{ d.fn }}-big.jpg" target="_blank">
        <img src="{{ d.fn }}-small.jpg" />
    </a>
</div>
{% endfor %}

<!--more-->



Reference:

