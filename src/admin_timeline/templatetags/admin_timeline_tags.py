__title__ = 'admin_timeline.templatetags.admin_timeline_tags'
__version__ = '0.8'
__build__ = 0x000008
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__all__ = ('assign',)

from django import template

register = template.Library()

class AssignNode(template.Node):
    """
    Node for ``assign`` tag.
    """
    def __init__(self, value, as_var):
        self.as_var = as_var
        self.value = value

    def render(self, context):
        context[self.as_var] = self.value.resolve(context, True)
        return ''

@register.tag
def assign(parser, token):
    """
    Assign an expression to a variable in the current context.

    Syntax::
        {% assign [value] as [name] %}
    Example::
        {% assign entry.get_related as list %}
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise template.TemplateSyntaxError("'%s' tag takes three arguments" % bits[0])
    value = parser.compile_filter(bits[1])
    return AssignNode(as_var=bits[-1], value=value)
