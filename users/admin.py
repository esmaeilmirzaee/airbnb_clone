from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomAdminUser(UserAdmin):
    list_display = ('username', 'superhost', 'language', 'currency',)
    list_filter = ('superhost',)

    fieldsets = UserAdmin.fieldsets + (
            ("Change portfolio", {
                    "fields": ('avatar', 'gender', 'birthdate', 'bio', 'currency', 'language')
            }),
    )


# admin.site.register(models.User, CustomAdminUser)
