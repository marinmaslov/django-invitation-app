from django.db import models
from django.utils.crypto import get_random_string
import datetime

# Invitation Model
class Invitation(models.Model):
    slug = models.CharField(unique=True, max_length=8, default=get_random_string(length=8))
    created = models.DateTimeField(default=datetime.datetime.now())
    confirmed = models.BooleanField(default=False)
    isFamily = models.BooleanField(default=False)

    def __str__(self):
        return str(self.slug)

# Guests Model
class Guest(models.Model):
    name = models.CharField(default="", max_length=50)
    surname = models.CharField(default="", max_length=50)
    phone = models.IntegerField(default="")
    email = models.EmailField(default="")
    invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE)

# Escort Model
class Escort(models.Model):
    name = models.CharField(default="", max_length=50)
    surname = models.CharField(default="", max_length=50)
    phone = models.IntegerField(default="")
    email = models.EmailField(default="")
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
