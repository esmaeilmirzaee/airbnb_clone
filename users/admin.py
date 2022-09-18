from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomAdminUser(UserAdmin):
    list_display = ('username', 'superhost', 'get_language', 'currency', 'is_active', 'is_staff', 'is_superuser',)
    list_filter = ('superhost',)

    fieldsets = UserAdmin.fieldsets + (
            ("Change portfolio", {
                    "fields": ('avatar', 'gender', 'birthdate', 'bio', 'currency', 'language')
            }),
    )

    list_filter = UserAdmin.list_filter + (
        'superhost',
        'language',
    )

    def get_language(self, obj):
        return obj.language.upper()


# admin.site.register(models.User, CustomAdminUser)
