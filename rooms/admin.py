from django.contrib import admin
from . import models


@admin.register(models.TypeOfRoom)
class TypeOfRoomAdmin(admin.ModelAdmin):
    ...


class RoomsAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Room, RoomsAdmin)
