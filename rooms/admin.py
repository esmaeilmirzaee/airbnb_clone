from django.contrib import admin
from . import models


class RoomsAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Room, RoomsAdmin)
