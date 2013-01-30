from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'qa.main.views.index', name='index'),
    url(r'^home/$', 'qa.main.views.home', name='home'),
    url(r'^check_qa/$', 'qa.main.views.check_qa', name='check_qa'),
    url(r'^save_profile/$', 'qa.main.views.save_profile', name='save_profile'),

    url(r'^accounts/', include('userena.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
