#coding=utf-8

from django.db import models
from django.core.exceptions import ValidationError
# Create your moels here.


class Beacon(models.Model):
    uuid = models.CharField(max_length=255, null=False, blank=True)
    major = models.IntegerField()
    minor = models.IntegerField()
    frequency = models.BigIntegerField(null=True, blank=True)
    object = models.ForeignKey('Object')
    description = models.CharField(max_length=255)
    point = models.ForeignKey('Point', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.description)

    def clean(self):
        if self.object_id is None and self.point_id is None:
            raise ValidationError("Object and Point are both null for %s %d %d beacon" % (self.uuid, self.major, self.minor))
        if self.object_id is not None and self.point_id is not None:
            raise ValidationError("Both Object and Point exist for beacon %s %d %d beacon" % (self.uuid, self.major, self.minor))
        return


class Point(models.Model):
    x = models.FloatField(default=0, null=False)
    y = models.FloatField(default=0, null=False)
    z = models.FloatField(default=0, null=False)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        s = ""
        if self.description is not None:
            s = self.description
        return unicode("%s. (%f, %f, %f)" % (s, self.x, self.y, self.z))


class Object(models.Model):
    description = models.CharField(max_length=255, null=True)
    descriptionFar = models.CharField(max_length=255, null=False)
    descriptionNear = models.CharField(max_length=255, null=False)
    descriptionImmediate = models.CharField(max_length=255, null=False)
    point = models.ForeignKey('Point')

    def __unicode__(self):
        return self.description