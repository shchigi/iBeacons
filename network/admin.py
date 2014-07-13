__author__ = 'rakot'

from django.contrib import admin
from models import Object, Beacon, Point


admin.site.register(Object)
admin.site.register(Beacon)
admin.site.register(Point)
