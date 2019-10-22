from django.contrib import admin
from django.urls import path, include

from .views import get_invitations

urlpatterns = [
    path('', get_invitations),
]
