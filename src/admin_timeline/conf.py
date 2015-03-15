__title__ = 'admin_timeline.conf'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('get_setting',)

from django.conf import settings

from admin_timeline import defaults

def get_setting(setting, override=None):
    """
    Get a setting from ``admin_timeline`` conf module, falling back to the
    default.

    If override is not None, it will be used instead of the setting.

    :param setting: String with setting name
    :param override: Value to use when no default setting is available.
        Defaults to None.
    :return: Setting value.
    """
    if override is not None:
        return override
    _setting = 'ADMIN_TIMELINE_{0}'.format(setting)
    if hasattr(settings, _setting):
        return getattr(settings, _setting)
    else:
        return getattr(defaults, setting)
