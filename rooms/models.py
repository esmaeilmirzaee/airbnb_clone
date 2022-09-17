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
    pass


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
    room_type = models.ManyToManyField(TypeOfRoom, blank=True)

    def __str__(self):
        return self.name
