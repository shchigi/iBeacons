__author__ = 'rakot'

from models import Beacon, Object
from rest_framework import serializers
from django.http import HttpResponse
from rest_framework.renderers import UnicodeJSONRenderer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = UnicodeJSONRenderer().render(data)
        kwargs['content_type'] = 'application/json; indent=4; charset=utf-8'
        super(JSONResponse, self).__init__(content, **kwargs)


class BeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beacon
        fields = ('uuid',
                  'major',
                  'minor')

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ('description',
                  'description_near',
                  'description_far',
                  'description_immediate')