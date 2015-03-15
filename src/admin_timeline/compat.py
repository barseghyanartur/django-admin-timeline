__title__ = 'admin_timeline.compat'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('TEMPLATE_NAME', 'TEMPLATE_NAME_AJAX',)

from nine.versions import DJANGO_LTE_1_4

TEMPLATE_NAME = "admin_timeline/timeline.html"
TEMPLATE_NAME_AJAX = "admin_timeline/timeline_ajax.html"

if DJANGO_LTE_1_4:
    TEMPLATE_NAME = "admin_timeline/django_lte14/timeline.html"
    TEMPLATE_NAME_AJAX = "admin_timeline/django_lte14/timeline_ajax.html"
