from django.db import models
from django.utils import timezone
from core.models import TimeStampedModel


class Reservation(TimeStampedModel):
    STATUS_PENDING = 'pending'
    STATUS_CANCELLED = 'cancelled'
    STATUS_SUCCESS = 'success'

    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_SUCCESS, 'Success'),
    )

    status = models.CharField(max_length=12, default=STATUS_PENDING, choices=STATUS_CHOICES)
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
    guest = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room.name[:8]} | {self.status}'

    def in_progress(self):
        now = timezone.now().date()

        return self.check_in < now < self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return self.check_out < now

    is_finished.boolean = True
