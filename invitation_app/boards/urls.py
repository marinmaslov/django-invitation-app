from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import path, include

#from .views import AdminBoardView

urlpatterns = [
    #path('board/<slug:board_name>', login_required(AdminBoardView.as_view()), name='board'),
    #path(),
    
]