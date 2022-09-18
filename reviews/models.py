from django.db import models

from core.models import TimeStampedModel


class Review(TimeStampedModel):
    content = models.TextField()
    accuracy = models.DecimalField()
    cleanliness = models.DecimalField()
    communication = models.DecimalField()
    location = models.DecimalField()
    check_in = models.DecimalField()
    value = models.DecimalField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
