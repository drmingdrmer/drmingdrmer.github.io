---
layout: post
title:  "Vim-tabbar: Simple, stupid and fast tab-bar for VIM"
date:   2015 Feb 11
categories: tech vim
tags: vim tab plugin
---

<iframe src="https://ghbtns.com/github-btn.html?user=drmingdrmer&repo=vim-tabbar&type=star&count=true&size=large"
        frameborder="0" scrolling="0"
        width="170px" height="30px"
        ></iframe>
Simple, stupid and fast tab-bar for VIM.

Names of opened buffer are shortened and shows on the top row of window.

Tab button uses one of these three highlight for different states:

-   `TabLineFill`: inactive buffer(**grey text on cyan background**).
-   `TabLine`: in one of the windows but not focused(**white text on dark cyan background**).
-   `TabLineSel`: currently focused buffer(**black text on white background**).

![](/img/vim-tabbar/screenshot.png)

##  Installation

Installing with [pathogen.vim](https://github.com/tpope/vim-pathogen)
 is recommended. Copy and paste:

```sh
cd ~/.vim/bundle
git clone git://github.com/drmingdrmer/vim-tabbar.git
```

Or just copy all of the files in to `~/.vim`.

##  Customizing Colors

Three high light settings in color scheme file(`~/.vim/colors/**.vim`)
are used by this plugin:

```vim
hi TabLineFill cterm=none ctermfg=grey  ctermbg=cyan
hi TabLine     cterm=none ctermfg=white ctermbg=cyan
hi TabLineSel  cterm=none ctermfg=black ctermbg=white
```

Check out on github:
[vim-tabbar][vim-tabbar].

[vim-tabbar]: https://github.com/drmingdrmer/vim-tabbar
