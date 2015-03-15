__title__ = 'admin_timeline.urls'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('urlpatterns',)

from django.conf.urls import url

from admin_timeline.views import log

urlpatterns = [
    url(r'^$', view=log, name='admin_timeline.log'),
]
