# Create your views here.

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from network.models import Beacon
from rest_api_handler import BeaconSerializer
import json


@api_view(['GET'])
def beacon_uuids(request, format=None):
    if request.method == 'GET':
        uuids = list(Beacon.objects.values_list('uuid', flat=True).distinct())
        return Response(uuids)


# @api_view(['GET'])
# def beacon_details(request, beacon_id, format=None):
#     if request.method == 'GET':
#         beacon = Beacon.objects.get(id=beacon_id)
#         serializer = BeaconSerializer(beacon)
#         return Response(serializer.data)

