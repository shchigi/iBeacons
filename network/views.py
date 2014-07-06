# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from network.models import Beacon
from rest_api_handler import BeaconSerializer


@api_view(['GET', 'POST'])
def beacon_list(request, format=None):
    if request.method == 'GET':
        beacons = Beacon.objects.all()
        serializer = BeaconSerializer(beacons, many=True)
        return Response(serializer.data)

