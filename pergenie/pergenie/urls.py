from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pergenie.views.home', name='home'),
    # url(r'^pergenie/', include('pergenie.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'apps.frontend.views.index'),
    url(r'^login/$', 'apps.frontend.views.login'),
    url(r'^logout/$', 'apps.frontend.views.logout'),
    url(r'^register/$', 'apps.frontend.views.register'),
    url(r'^settings/$', 'apps.frontend.views.settings'),
    url(r'^about/$', 'apps.frontend.views.about'),

    url(r'^dashboard/$', 'apps.dashboard.views.index'),

    url(r'^riskreport/$', 'apps.riskreport.views.index'),
    url(r'^riskreport/(?P<file_name>.*?)/(?P<trait>.*?)/$', 'apps.riskreport.views.trait'),

    url(r'^library/$', 'apps.library.views.index'),
    url(r'^library/summary', 'apps.library.views.summary'),
    url(r'^library/trait/$', 'apps.library.views.trait_index'),
    url(r'^library/trait/(?P<trait>.*?)/$', 'apps.library.views.trait'),
    url(r'^library/snps/$', 'apps.library.views.snps_index'),
    url(r'^library/snps/rs(?P<rs>.*?)/$', 'apps.library.views.snps'),

    url(r'^upload/$', 'apps.upload.views.index'),
    url(r'^upload/delete', 'apps.upload.views.delete'),
    url(r'^upload/status', 'apps.upload.views.status'),
)
