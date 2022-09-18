from django.db import models

from core.models import TimeStampedModel


class Review(TimeStampedModel):
    content = models.TextField()
    accuracy = models.DecimalField(decimal_places=1, max_digits=2)
    cleanliness = models.DecimalField(decimal_places=1, max_digits=2)
    communication = models.DecimalField(decimal_places=1, max_digits=2)
    location = models.DecimalField(decimal_places=1, max_digits=2)
    check_in = models.DecimalField(decimal_places=1, max_digits=2)
    value = models.DecimalField(decimal_places=1, max_digits=2)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room} by {self.user.username.upper()}'
