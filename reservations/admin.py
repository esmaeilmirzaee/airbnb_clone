from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('room', 'check_in', 'check_out', 'status', 'in_progress', 'is_finished',)
