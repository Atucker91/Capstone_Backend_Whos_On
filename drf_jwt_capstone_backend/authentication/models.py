from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    middle_name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=20)
    band_name = models.CharField(max_length=100)
    venue_name = models.CharField(max_length=100)
    is_band = models.BooleanField(default=False)
    is_venue = models.BooleanField(default=False)
