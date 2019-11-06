from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from .views import UserProfileView

urlpatterns = [
    #path('board/<slug:board_name>', login_required(AdminBoardView.as_view()), name='board'),
    #path(),

    

    path('u/<slug:username>/dashboard/', login_required(UserProfileView.as_view()), name='dashboard'),

    path('u/<slug:username>/boards/', login_required(UserProfileView.as_view()), name='boards'),

    #path('u/<slug:username>/boards/<slug:boardname>', login_required(UserProfileView.as_view()), name='profile'),

    #path('u/<slug:username>/boards/<slug:boardname>/<slug:invitation>', login_required(UserProfileView.as_view()), name='profile'),

]