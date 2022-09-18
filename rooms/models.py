from django.db import models
from django_countries.fields import CountryField

from core import models as core_model
from users import models as user_model


class AbstractItem(core_model.TimeStampedModel):

    name = models.CharField(max_length=90)
    description = models.CharField(max_length=130, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class TypeOfRoom(AbstractItem):
    class Meta:
        verbose_name = 'Type of Room'
        ordering = ['name']


class Amenity(AbstractItem):
    class Meta:
        verbose_name_plural = 'Amenities'


class HouseRule(AbstractItem):
    class Meta:
        verbose_name = 'House Rule'


class Facility(AbstractItem):
    class Meta:
        verbose_name_plural = 'Facilities'


class Photo(core_model.TimeStampedModel):
    caption = models.CharField(max_length=100)
    file = models.ImageField(upload_to='images')
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Photo'

    def __str__(self):
        return self.caption


class Room(core_model.TimeStampedModel):
    """Room Model"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=150)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_model.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(TypeOfRoom, on_delete=models.SET_NULL, null=True, blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):
        return self.name
