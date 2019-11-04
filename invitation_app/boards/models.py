from django.db import models

from django.utils.crypto import get_random_string
import datetime

from users.models import Profile

# Board Model
class Board(models.Model):
    name = models.CharField(default="", max_length=50)
    image = models.ImageField(default='default-boards.jpg', upload_to='static/img/boards/')
    date_created = models.DateTimeField(default=datetime.datetime.now())
    laste_modified = models.DateTimeField(default=datetime.datetime.now())
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name)

# Invitation Model
class Invitation(models.Model):
    created = models.DateTimeField(default=datetime.datetime.now(), blank=True, null=True)
    slug = models.CharField(unique=True, max_length=8, default=get_random_string(length=8))
    name = models.CharField(default="", max_length=50)
    surname = models.CharField(default="", max_length=50)
    email = models.EmailField(default="")
    phone = models.IntegerField(default="")
    confirmed = models.BooleanField(default=False)
    confirmation_date = models.DateTimeField(default=datetime.datetime.now())
    multiple_escort = models.BooleanField(default=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

# Escort Model
class Escort(models.Model):
    name = models.CharField(default="", max_length=50)
    surname = models.CharField(default="", max_length=50)
    # MOZDA BI CAK UKLONIA I OVAJ DIO
    phone = models.IntegerField(default="")
    email = models.EmailField(default="")
    invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE)