__author__ = 'rakot'

from django.conf.urls import patterns, url, include
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'^docs/',
        include('rest_framework_swagger.urls')),

    url(r'uuids/$',
        'network.views.beacon_uuids',
        name="beacon_uuids"),

    # /object/05346cc3-7659-4cd8-ae3e-b5e983cde94c/12/2/
    url(r'object/(?P<uuid>[-\w]+?)/(?P<major>\d+?)/(?P<minor>\d+?)/$',
        'network.views.objects_from_beacons',
        name='objects_from_beacons'),

    url(r'events/(?P<object_id>\d+?)/$',
        'network.views.events_from_object')

)

# urlpatterns = format_suffix_patterns(urlpatterns)
