# from django.contrib import admin
from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin

from .models import Location, Area

# Register your models here.


class LocationAdmin(LeafletGeoAdmin):

    list_display = ('name', 'point')


admin.site.register(Location, LocationAdmin)


class AreaAdmin(LeafletGeoAdmin):

    list_display = ('name', 'polygon')


admin.site.register(Area, AreaAdmin)
