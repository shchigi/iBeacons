__author__ = 'rakot'

from django.conf.urls import patterns, url
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'beacons/$', 'network.views.beacon_list'),
)

# urlpatterns = format_suffix_patterns(urlpatterns)