from django.db import models
from core import models as core_models


class Wishlists(core_models.TimeStampedModel):
    """ Wish and experience list """
    name = models.CharField(max_length=80)
    rooms = models.ManyToManyField('rooms.Room')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.rooms.count()}'

    def number_of_rooms(self):
        return f'{self.rooms.count()}'
