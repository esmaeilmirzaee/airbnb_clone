from django.contrib import admin
from . import models


@admin.register(models.Wishlists)
class WishlistsAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'number_of_rooms',)
    search_fields = ('name',)
    filter_horizontal = ('rooms',)
