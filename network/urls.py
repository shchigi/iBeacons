__author__ = 'rakot'

from django.conf.urls import patterns, url
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'uuids/$', 'network.views.beacon_uuids'),
    # /object/05346cc3-7659-4cd8-ae3e-b5e983cde94c/12/2/
    url(r'object/(?P<uuid>[-\w]+?)/(?P<major>\d+?)/(?P<minor>\d+?)/$', 'network.views.objects_from_beacons')
)

# urlpatterns = format_suffix_patterns(urlpatterns)