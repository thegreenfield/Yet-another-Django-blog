from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import django

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': django.__path__[0] + '/contrib/admin/media', 'show_indexes' : True}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
)
