from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    postal_code = models.CharField(max_length=20)
    is_band = models.BooleanField(default=False)
    is_venue = models.BooleanField(default=False)
    profile_img = models.CharField(max_length=200)


class Band(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    band_name = models.CharField(max_length=100)
    song_to_display = models.CharField(max_length=200)


class Venue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    venue_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class FollowingBands(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    band_id = models.ForeignKey(Band, on_delete=models.CASCADE)


class FollowingVenues(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    venue_id = models.ForeignKey(Venue, on_delete=models.CASCADE)
