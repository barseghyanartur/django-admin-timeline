__all__ = ('urlpatterns',)

from django.conf.urls import patterns, url

urlpatterns = patterns('admin_timeline.views',
    url(r'^$', view='log', name='admin_timeline.log'),
)
