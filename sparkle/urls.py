from django.conf.urls.defaults import *

urlpatterns = patterns('sparkle.views',
    url(r'^(?P<application_id>\d+)/appcast.xml$', 'appcast', name='sparkle_application_appcast'),
    url(r'^(?P<slug>[\w-]+)/appcast.xml$', 'appcast', name='sparkle_application_appcast_slug'),
)
