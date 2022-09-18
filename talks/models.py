from django.db import models
from core.models import TimeStampedModel


class Talk(TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    participants = models.ForeignKey('Participants', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.message[:12]}'


class Participants(TimeStampedModel):
    actor = models.ManyToManyField('users.User')

    def __str__(self):
        return f'{self.actor.count()} @ {self.created_at.date()}'
