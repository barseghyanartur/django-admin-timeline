from django.conf.urls import url

from .views import log

__title__ = 'admin_timeline.urls'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('urlpatterns',)


urlpatterns = [
    url(r'^$', view=log, name='admin_timeline.log'),
]
