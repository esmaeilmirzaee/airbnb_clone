from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomAdminUser(admin.ModelAdmin):
    list_display = ('username', 'superhost', 'language', 'currency',)
    list_filter = ('superhost',)


# admin.site.register(models.User, CustomAdminUser)
