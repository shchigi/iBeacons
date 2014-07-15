__author__ = 'rakot'

from django.contrib import admin
from models import Object, Beacon, InnerPoint, OuterPoint


admin.site.register(Object)
admin.site.register(Beacon)
admin.site.register(InnerPoint)
admin.site.register(OuterPoint)
