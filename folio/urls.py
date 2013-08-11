from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'folio.views.home', name='home'),
    # url(r'^folio/', include('folio.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
