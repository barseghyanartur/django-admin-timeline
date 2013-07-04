__title__ = 'admin_timeline.conf'
__version__ = '0.8'
__build__ = 0x000008
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__all__ = ('get_setting',)

from django.conf import settings

from admin_timeline import defaults

def get_setting(setting, override=None):
    """
    Get a setting from "admin_timeline" conf module, falling back to the default.

    If override is not None, it will be used instead of the setting.

    :param setting: String with setting name
    :param override: Value to use when no setting is available. Defaults to None.
    :return: Setting value.
    """
    if override is not None:
        return override
    if hasattr(settings, 'ADMIN_TIMELINE_%s' % setting):
        return getattr(settings, 'ADMIN_TIMELINE_%s' % setting)
    else:
        return getattr(defaults, setting)
