from django import forms
from django.contrib.admin.models import LogEntry

__title__ = 'admin_timeline.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'get_users',
    'get_content_types',
    'FilterForm',
)


def get_users(data):
    """Get user choices."""
    return list(
        set(
            [
                (
                    __d.user_id, __d.user.get_full_name()
                    if __d.user.get_full_name()
                    else __d.user.username
                ) for __d in data
            ]
        )
    )


def get_content_types(data):
    """Get content type choices."""
    return list(
        set(
            [
                (
                    (__d.content_type_id, __d.content_type.name)
                    if __d.content_type_id
                    else (None, "")
                )
                for __d
                in data
            ]
        )
    )


class FilterForm(forms.Form):
    """Filter form to be used in the timeline.

    ``users``: Users list to be filtered on.

    ``content_types``: Content types to be filtered on.
    """
    def __init__(self, *args, **kwargs):
        # Getting a plain list of all users who have done anything.
        data = LogEntry.objects \
                       .all() \
                       .select_related('user', 'content_type') \
                       .only('content_type', 'user')[:]

        super(FilterForm, self).__init__(*args, **kwargs)

        self.fields['users'] = forms.MultipleChoiceField(
            choices=get_users(data),
            # widget=forms.CheckboxSelectMultiple,
            required=False
        )
        self.fields['content_types'] = forms.MultipleChoiceField(
            choices=get_content_types(data),
            # widget=forms.CheckboxSelectMultiple,
            required=False
        )
