from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Our custom user model"""
    MALE_GENDER = 'male'
    FEMALE_GENDER = 'female'
    RATHER_GENDER = 'rather'

    GENDER_CHOICES = (
        (MALE_GENDER, 'Male'),
        (FEMALE_GENDER, 'female'),
        (RATHER_GENDER, 'Rather Not Say'),
    )

    avatar = models.ImageField(null=True)
    bio = models.TextField(default='')
    gender = models.CharField(max_length=10, null=True, choices=GENDER_CHOICES)

