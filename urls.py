#coding=utf-8
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
from django.contrib.auth.views import login, logout
from BusLove import settings
from BusLove.bus.views import index
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    # url(r'^BusLove/', include('BusLove.foo.urls')),
    (r'^accounts/login/$',login,{'template_name':'login.html'}),
    (r'^accounts/logout/$', logout,{'template_name':'logout.html'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),

#    url(r'^admin/', include(admin.site.urls)),
)
