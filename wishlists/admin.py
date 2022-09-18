from django.contrib import admin
from . import models


@admin.register(models.Wishlists)
class WishlistsAdmin(admin.ModelAdmin):
    ...
