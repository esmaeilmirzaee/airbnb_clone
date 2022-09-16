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

    CURRENCY_USA = 'usd'
    CURRENCY_PERSIAN = 'irl'

    CURRENCY_CHOICES = ((CURRENCY_USA, 'USD'), (CURRENCY_PERSIAN, 'IRL'))

    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_PERSIAN = 'fa'

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, 'en'), (LANGUAGE_PERSIAN, 'fa'))

    avatar = models.ImageField(null=True, required=False)
    bio = models.TextField(default='', null=True)
    gender = models.CharField(max_length=14, null=True, choices=GENDER_CHOICES, default=RATHER_GENDER)
    birthday = models.DateField(null=True, required=False)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=CURRENCY_USA)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default=LANGUAGE_ENGLISH)
