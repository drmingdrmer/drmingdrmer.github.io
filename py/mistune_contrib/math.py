# coding: utf-8

"""
    mistune_contrib.math
    ~~~~~~~~~~~~~~~~~~~~

    Support Math features for mistune.

    :copyright: (c) 2014 by Hsiaoming Yang.
"""

import re


class MathBlockMixin(object):
    """Math mixin for BlockLexer, mix this with BlockLexer::

        class MathBlockLexer(MathBlockMixin, BlockLexer):
            def __init__(self, *args, **kwargs):
                super(MathBlockLexer, self).__init__(*args, **kwargs)
                self.enable_math()
    """
    def enable_math(self):
        self.rules.block_math = re.compile(r'^\$\$(.*?)\$\$', re.DOTALL)
        self.rules.block_latex = re.compile(
            r'^\\begin\{([a-z]*\*?)\}(.*?)\\end\{\1\}', re.DOTALL
        )

        # block_math must come before paragraph, or it is rendered as a normal paragraph
        rs = self.default_rules
        i = rs.index('paragraph')
        rs.insert(i, 'block_latex')
        rs.insert(i, 'block_math')

    def parse_block_math(self, m):
        """Parse a $$math$$ block"""
        self.tokens.append({
            'type': 'block_math',
            'text': m.group(1)
        })

    def parse_block_latex(self, m):
        self.tokens.append({
            'type': 'block_latex',
            'name': m.group(1),
            'text': m.group(2)
        })



class MathMarkdownMixin(object):

    # block level token requires a output_* function
    def output_block_math(self):
        body = '\n'
        body += self.renderer.block_math(self.token['text'])
        body += '\n'
        return body

    def output_block_latex(self):
        body = '\n'
        body += self.renderer.block_latex(self.token['name'],
                                          self.token['text'])
        body += '\n'
        return body

class MathInlineMixin(object):
    """Math mixin for InlineLexer, mix this with InlineLexer::

        class MathInlineLexer(InlineLexer, MathInlineMixin):
            def __init__(self, *args, **kwargs):
                super(MathInlineLexer, self).__init__(*args, **kwargs)
                self.enable_math()
    """

    def enable_math(self):
        self.rules.math = re.compile(r'^\$(.+?)\$')
        self.default_rules.insert(0, 'math')
        self.rules.text = re.compile(r'^[\s\S]+?(?=[\\<!\[_*`~\$]|https?://| {2,}\n|$)')

    def output_math(self, m):
        return self.renderer.math(m.group(1))


class MathRendererMixin(object):
    def block_math(self, text):
        # override with customized math rendering
        return '$$ math-renderer-mixin-block: %s$$' % text

    def block_latex(self, name, text):
        # override with customized math rendering
        return r' math-renderer-mixin-latex: \begin{%s}%s\end{%s}' % (name, text, name)

    def math(self, text):
        # override with customized math rendering
        return '$ math-renderer-mixin-inline: %s$' % text


if __name__ == "__main__":

    # Usage: define your own block-lexer, inline-lexer, markdown engine and
    # renderer to customize math rendering.

    from mistune import Markdown
    from mistune import BlockLexer
    from mistune import InlineLexer
    from mistune import Renderer

    class MathBlockLexer(MathBlockMixin, BlockLexer):
        def __init__(self, *args, **kwargs):
            super(MathBlockLexer, self).__init__(*args, **kwargs)
            self.enable_math()


    class MathInlineLexer(InlineLexer, MathInlineMixin):
        def __init__(self, *args, **kwargs):
            super(MathInlineLexer, self).__init__(*args, **kwargs)
            self.enable_math()


    class MathRenderer(Renderer, MathRendererMixin):
        pass


    class MathMarkdown(Markdown, MathMarkdownMixin):
        pass

    render = MathRenderer()
    md = MathMarkdown(render,
                      inline=MathInlineLexer(render),
                      block=MathBlockLexer
    )

    print md('''
block math:

$$
y = x^2
$$

inline math: $ y = \\frac{1}{x} $''')

    # output:
    #     <p>block math:</p>
    #
    #     $$ this is my math:
    #     y = x^2
    #     $$
    #     <p>inline math: $ this is my math:  y = \frac{1}{x} $</p>
