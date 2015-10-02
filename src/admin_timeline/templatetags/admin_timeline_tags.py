__title__ = 'admin_timeline.templatetags.admin_timeline_tags'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('assign', 'get_full_name', 'resolve_admin_url',)

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch

from nine.versions import DJANGO_GTE_1_7

if DJANGO_GTE_1_7:
    from django.contrib.admin.utils import quote
else:
    from django.contrib.admin.util import quote

register = template.Library()

class AssignNode(template.Node):
    """
    Node for ``assign`` tag.
    """
    def __init__(self, value, as_var):
        self.value = value
        self.as_var = as_var

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
        raise template.TemplateSyntaxError("'{0}' tag takes "
                                           "three arguments".format(bits[0]))
    value = parser.compile_filter(bits[1])
    return AssignNode(value=value, as_var=bits[-1])


class GetFullNameNode(template.Node):
    """
    Node for ``get_full_name`` tag.
    """
    def __init__(self, user, as_var):
        self.user = user
        self.as_var = as_var

    def render(self, context):
        user = self.user.resolve(context, True)
        context[self.as_var] = user.get_full_name() or user.username
        return ''

@register.tag
def get_full_name(parser, token):
    """
    Get users' full name.

    Syntax::
        {% get_full_name [user] as [name] %}
    Example::
        {% get_full_name entry.user as user_full_name %}
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise template.TemplateSyntaxError("'{0}' tag takes "
                                           "three arguments".format(bits[0]))
    user = parser.compile_filter(bits[1])
    return GetFullNameNode(user=user, as_var=bits[-1])

@register.filter
def resolve_admin_url(entry):
    if entry.content_type and entry.object_id:
        url_name = 'admin:%s_%s_change' % (entry.content_type.app_label,
                                           entry.content_type.model)
        try:
            return reverse(url_name, args=(quote(entry.object_id),))
        except NoReverseMatch:
            pass
    return None
