import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.codehilite import CodeHiliteExtension


class Markdown(object):

    md = markdown.Markdown(extensions=[FencedCodeExtension(), CodeHiliteExtension()])

    @classmethod
    def convert(cls, *args, **kwargs):
        return cls.md.convert(*args, **kwargs)
