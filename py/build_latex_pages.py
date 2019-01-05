#!/usr/bin/env python2
# coding: utf-8

import base64
import os
import re
import sys

from mistune import BlockGrammar
from mistune import BlockLexer
from mistune import InlineLexer
from mistune import Markdown
from mistune import Renderer

from mistune_contrib import math as mmath
from pykit import proc


def dd(*msg):
    print ''.join([str(x) for x in msg])


class MathBlockLexer(mmath.MathBlockMixin, BlockLexer):
    def __init__(self, *args, **kwargs):
        super(MathBlockLexer, self).__init__(*args, **kwargs)
        self.enable_math()


class MathInlineLexer(InlineLexer, mmath.MathInlineMixin):
    def __init__(self, *args, **kwargs):
        super(MathInlineLexer, self).__init__(*args, **kwargs)
        self.enable_math()


class MathRenderer(Renderer):

    def block_math(self, text):
        return self.math(text, quote='$$')

    def block_latex(self, name, text):
        return r'\begin{%s}%s\end{%s}' % (name, text, name)

    def math(self, text, quote='$'):

        # remove empty line those annoy pdflatex
        text = re.sub('\n *\n', '\n', text)

        tex = ('\\documentclass{article}\n'
               '\\pagestyle{empty}\n'
               '\\begin{document}\n'
               '%s%s%s\n'
               '\end{document}') % (quote, text, quote)

        basefn = 'xp-blog-tmp'
        texfn = basefn + '.tex'
        pdffn = basefn + '.pdf'
        croppedfn = basefn + '-crop.pdf'

        with open(texfn, 'w') as f:
            f.write(tex)

        proc.command_ex('pdflatex', texfn)
        proc.command_ex('pdfcrop', pdffn, croppedfn)
        rc, pngdata, err = proc.command_ex(
            'convert',
            '-density', '160',
            '-quality', '100',
            croppedfn, 'png:-'
        )

        datauri = "data:{};base64,{}".format('image/png',
                                             base64.b64encode(pngdata))
        tooltip = text.replace('"', '&quot;')

        img = '<img style="vertical-align: bottom; display: inline;" src="{datauri}" alt="{alt}" title="{title}"/>'.format(
            datauri=datauri,
            title=tooltip,
            alt=tooltip,
        )

        for fn in (croppedfn,
                   pdffn,
                   texfn,
                   basefn + '.log',
                   basefn + '.aux',
                   ):
            try:
                os.unlink(fn)
            except EnvironmentError as e:
                pass

        dd('built latex ', repr(text))
        return img


class MathMarkdown(Markdown):

    def output_block_math(self):
        body = '\n'
        body += self.renderer.block_math(self.token['text'])
        body += '\n'
        return body


def build_page(srcpath, dstpath=None):

    with open(srcpath, 'r') as f:
        cont = f.read()

    # find the second '---\n'
    start = cont.index('---\n', 4)
    head = cont[:start+4]
    body = cont[start+4:]

    render = MathRenderer()
    inline = MathInlineLexer(render)
    md = MathMarkdown(render,
                      inline=inline,
                      block=MathBlockLexer
                      )

    html = md(body)
    html = head + html

    if dstpath is not None:
        with open(dstpath, 'w') as f:
            f.write(html)

    return html


if __name__ == "__main__":
    src = sys.argv[1]
    if len(sys.argv) > 2:
        dst = sys.argv[2]
    else:
        dst = None

    x = build_page(src, dst)

    if dst is None:
        print x
