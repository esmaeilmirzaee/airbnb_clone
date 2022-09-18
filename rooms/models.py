import decimal

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
    room = models.ForeignKey('Room', related_name='photos', on_delete=models.CASCADE)

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
    host = models.ForeignKey(user_model.User, related_name='rooms', on_delete=models.CASCADE)
    room_type = models.ForeignKey(TypeOfRoom, related_name='rooms', on_delete=models.SET_NULL, null=True, blank=True)
    amenities = models.ManyToManyField(Amenity, related_name='rooms', blank=True)
    facilities = models.ManyToManyField(Facility, related_name='rooms', blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name='rooms', blank=True)

    def __str__(self):
        return self.name

    def total_ratings(self):
        all_reviews = self.reviews.all()
        total_rating = 0
        for review in all_reviews:
            total_rating += review.rating_average()

        total_avg = total_rating / len(all_reviews)

        return round(total_avg, 2)
