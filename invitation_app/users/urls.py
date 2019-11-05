from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required

from .views import register, UserProfileView

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('users/<slug:username>', login_required(UserProfileView.as_view()), name='profile'),
]