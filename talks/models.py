from django.db import models
from core.models import TimeStampedModel


class Talk(TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey('users.User', related_name='talk', on_delete=models.CASCADE)
    participants = models.ForeignKey('Participants', related_name='talk', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.message[:12]}'


class Participants(TimeStampedModel):
    actor = models.ManyToManyField('users.User', related_name='participant')

    def __str__(self):
        usernames = []
        for user in self.actor.all():
            usernames.append(user.username)

        return f'{", ".join(usernames)} @{self.created_at.date()} [{self.actor.count()}]'

    def number_of_messages(self):
        return self.talk.count()

    def number_of_participants(self):
        return self.actor.count()