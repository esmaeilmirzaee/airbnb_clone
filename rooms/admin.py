from django.contrib import admin

from . import models


@admin.register(models.TypeOfRoom, models.HouseRule, models.Facility, models.Amenity)
class TypeOfRoomAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'used_by',
    )

    def used_by(self, obj):
        return obj.rooms.count()


class RoomsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'room_type',
        'city',
        'country',
        'price',
        'instant_book',
        'number_of_amenities',
        'number_of_photos',
    )

    fieldsets = (
        (
            'Basic Info',
            {'fields': ('name', 'country', 'city', 'price',)}
        ),
        (
            'Spaces',
            {'fields': ('baths', 'beds', 'bedrooms')}
        ),
        (
            'Date and Time',
            {
                'fields': ('check_in', 'check_out', 'instant_book',)
            }
        ),
        (
            'Owner',
            {'fields': ('host',)}
        ),
        (
            'More About the Spaces',
            {
                'classes': ('collapse',),
                'fields': ('amenities', 'facilities', 'house_rules',),
            }
        ),
    )

    ordering = ('name', 'country',)
    list_filter = ('country', 'city',)
    search_fields = ('city', '=name', '^host__username')
    filter_horizontal = ("amenities", 'facilities', 'house_rules',)  # By default, just many to many

    def number_of_amenities(self, obj):
        return obj.amenities.count()

    number_of_amenities.short_description = 'Number of Amenities'

    def number_of_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    ...


admin.site.register(models.Room, RoomsAdmin)
