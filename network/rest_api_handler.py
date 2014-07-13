__author__ = 'rakot'

from models import Beacon, Point, Object
from rest_framework import serializers


class BeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beacon
        fields = ('uuid', 'major', 'minor', 'frequency', 'description')