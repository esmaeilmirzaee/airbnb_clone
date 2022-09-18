from django.contrib import admin
from . import models


@admin.register(models.TypeOfRoom, models.HouseRule, models.Facility, models.Amenity)
class TypeOfRoomAdmin(admin.ModelAdmin):
    ...


class RoomsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    ...



admin.site.register(models.Room, RoomsAdmin)
