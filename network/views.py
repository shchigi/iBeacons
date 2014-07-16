# Create your views here.

from rest_framework.decorators import api_view
from network.models import Beacon, InnerPoint, Object, Event
from network.rest_api_handler import EventSerializer
from rest_api_handler import JSONResponse, ObjectSerializer
from django.core.exceptions import ObjectDoesNotExist
import json

@api_view(['GET'])
def beacon_uuids(request, format=None):
    if request.method == 'GET':
        uuids = {"uuids": list(Beacon.objects.values_list('uuid', flat=True).distinct())}
        return JSONResponse(uuids, status=200)


# @api_view(['GET'])
# def beacon_details(request, beacon_id, format=None):
#     if request.method == 'GET':
#         beacon = Beacon.objects.get(id=beacon_id)
#         serializer = BeaconSerializer(beacon)
#         return Response(serializer.data)


@api_view(['GET'])
def objects_from_beacons(request, uuid, major, minor):
    # data = JSONParser().parse(request)
    # serializer = BeaconSerializer(data=data)
    # if serializer.is_valid():
    #     return JSONResponse(serializer.data, status=201)
    # request.encoding = 'utf-8'
    try:
        beacon = Beacon.objects.get(uuid=uuid, major=major, minor=minor)
        inner_point = InnerPoint.objects.get(beacon=beacon)
        object = Object.objects.get(innerpoint=inner_point)
        serializer = ObjectSerializer(object)
        return JSONResponse(serializer.data, status=200)
    except ObjectDoesNotExist as e:
        return JSONResponse(e.message, status=404)

def events_from_object(request, object_id):
    try:
        object = Object.objects.get(id=object_id)
        inner_poins = object.innerpoint_set.all()
        events = []
        for inner_point in inner_poins:
            e = Event.objects.filter(inner_point=inner_point)
            events.extend(e)
        print events
        serializer = EventSerializer(events, many=True)
        print "******"
        return JSONResponse({"events": serializer.data}, status=200)
    except ObjectDoesNotExist as e:
        return JSONResponse(e.message, status=404)
