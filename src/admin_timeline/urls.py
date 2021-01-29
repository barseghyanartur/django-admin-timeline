from django.conf.urls import re_path

from .views import log

__title__ = 'admin_timeline.urls'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2021 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('urlpatterns',)


urlpatterns = [
    re_path(r'^$', view=log, name='admin_timeline.log'),
]
