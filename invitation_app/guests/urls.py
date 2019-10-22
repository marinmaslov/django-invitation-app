from django.contrib import admin
from django.urls import path, include

from .views import GuestView #, get_invitations

urlpatterns = [
    #path('', get_invitations),
    path('guest/', GuestView.as_view()),
]
