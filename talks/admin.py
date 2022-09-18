from django.contrib import admin
from . import models


@admin.register(models.Talk)
class TalksAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at',)


class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'number_of_messages', 'number_of_participants',)


admin.site.register(models.Participants, ParticipantsAdmin)
