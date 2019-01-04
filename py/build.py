#!/usr/bin/env python2
# coding: utf-8

import os
import build_latex_pages

def build_math_posts():
    srcdir = '_tocompile'
    dstdir = '_posts'

    fns = os.listdir(srcdir)

    for fn in fns:
        build_latex_pages.build_page(
                os.path.join(srcdir, fn),
                os.path.join(dstdir, fn),
        )

if __name__ == "__main__":
    build_math_posts()
