from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'folio.views.index', name='index'),
    url(r'^contact.html$', 'folio.views.contact', name='contact'),
    url(r'^(?P<slug>[-\w]+).html$', 'folio.views.detail'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
