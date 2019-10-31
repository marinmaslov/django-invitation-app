from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path

from .views import MainView, AdminView, InvitationView

urlpatterns = [
    #path('', get_invitations),
    path('invitations/', MainView.as_view()),


    path('invitations/admin/', login_required(AdminView.as_view()), name='admin_main'),
    re_path(r'^invitations/admin/invitation/(?P<invitation_id>\d+)?$', InvitationView.as_view(), name='invitation'),
]
