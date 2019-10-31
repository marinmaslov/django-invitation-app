from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path

from .views import MainView, AdminView, AdminBoardView, AdminInvitationView

urlpatterns = [
    #path('', get_invitations),
    path('invitations/', MainView.as_view()),


    path('invitations/admin/', login_required(AdminView.as_view()), name='admin_main'),
    path('invitations/admin/board/', login_required(AdminBoardView.as_view()), name='admin_board'),
    re_path(r'^invitations/admin/board/invitation/(?P<invitation_id>\d+)?$', login_required(AdminInvitationView.as_view()), name='admin_invitation'),
]
