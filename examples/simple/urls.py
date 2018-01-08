from django.conf import settings
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin

from nine.versions import DJANGO_GTE_2_0

admin.autodiscover()

urlpatterns = [
    # django-admin-timeline URLs. Should come before the django-admin URLs.
    url(r'^admin/timeline/', include('admin_timeline.urls')),
]

if DJANGO_GTE_2_0:
    urlpatterns += [
        url(r'^admin/', admin.site.urls),
    ]
else:
    urlpatterns += [
        url(r'^admin/', include(admin.site.urls)),
    ]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    if settings.DEBUG_TOOLBAR:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
