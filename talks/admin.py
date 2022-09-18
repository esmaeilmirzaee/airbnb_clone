from django.contrib import admin
from . import models


@admin.register(models.Talk)
class TalksAdmin(admin.ModelAdmin):
    ...


class ParticipantsAdmin(admin.ModelAdmin):
    ...


admin.site.register(models.Participants, ParticipantsAdmin)
