from django.db import models
from django.utils.crypto import get_random_string
import datetime

# Board Model
class Board(models.Model):
    name = models.CharField(default="", max_length=50)

    def __str__(self):
        return str(self.name)

# Invitation Model
class Invitation(models.Model):
    created = models.DateTimeField(default=datetime.datetime.now())
    slug = models.CharField(unique=True, max_length=8, default=get_random_string(length=8))
    name = models.CharField(default="", max_length=50)
    surname = models.CharField(default="", max_length=50)
    email = models.EmailField(default="")
    phone = models.IntegerField(default="")
    confirmed = models.BooleanField(default=False)
    multiple_escort = models.BooleanField(default=False)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

# Escort Model
class Escort(models.Model):
    name = models.CharField(default="", max_length=50)
    surname = models.CharField(default="", max_length=50)
    phone = models.IntegerField(default="")
    email = models.EmailField(default="")
    invitation_id = models.ForeignKey(Invitation, on_delete=models.CASCADE)
