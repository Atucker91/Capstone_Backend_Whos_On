from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Venue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    venue_name = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
