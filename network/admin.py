__author__ = 'rakot'

from django.contrib import admin
from models import Object, Beacon, InnerPoint, OuterPoint, Person, Category, Event


admin.site.register(Object)
admin.site.register(Beacon)
admin.site.register(InnerPoint)
admin.site.register(OuterPoint)
admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Event)