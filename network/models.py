#coding=utf-8

from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


# describes points at streets like malls, business centers, etc
class OuterPoint(models.Model):
    lat = models.DecimalField(max_digits=11, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    description = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)

    def __unicode__(self):
        s = "" if self.description is None else self.description
        return unicode("%s; \n%s" % (self.name, s))


class Object(models.Model):
    description = models.CharField(max_length=255, null=True)
    description_far = models.CharField(max_length=255, null=False)
    description_near = models.CharField(max_length=255, null=False)
    description_immediate = models.CharField(max_length=255, null=False)
    outer_point = models.ForeignKey('OuterPoint', null=False, blank=False)
#   points available via object.point_set.all()

    def __unicode__(self):
        return self.description


# Describes points inside mall, business center, etc.
# Coordinates are for local coordinate system
# z included to indicate floors
class InnerPoint(models.Model):
    x = models.FloatField(default=0, null=False)
    y = models.FloatField(default=0, null=False)
    z = models.FloatField(default=0, null=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    # This is for one to many relationship with Object
    related_object = models.ForeignKey('Object', null=False, blank=False)

    def __unicode__(self):
        s = "" if self.description is None else self.description
        return unicode("%s. (%f, %f, %f)" % (s, self.x, self.y, self.z))


class Beacon(models.Model):
    uuid = models.CharField(max_length=255, null=False, blank=True)
    major = models.IntegerField()
    minor = models.IntegerField()
    frequency = models.BigIntegerField(null=True, blank=True)
    description = models.CharField(max_length=255)
    point = models.OneToOneField('InnerPoint', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.description)
