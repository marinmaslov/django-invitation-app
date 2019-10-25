from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from .views import GuestView, AdminView

urlpatterns = [
    #path('', get_invitations),
    path('', GuestView.as_view()),
    path('guests/admin/', login_required(AdminView.as_view()), name='admin_main'),
]
