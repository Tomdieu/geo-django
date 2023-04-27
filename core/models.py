from django.db import models
from django.contrib.gis.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    point = models.PointField(srid=4326)

    def __str__(self) -> str:
        return self.name


class Area(models.Model):

    name = models.CharField(max_length=255)
    polygon = models.PolygonField(srid=4326)

    def __str__(self) -> str:
        return self.name
