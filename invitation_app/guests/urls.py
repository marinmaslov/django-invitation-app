from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path

from .views import GuestView, AdminView, InvitationView

urlpatterns = [
    #path('', get_invitations),
    path('', GuestView.as_view()),
    re_path(r'^invitation/(?P<invitation_id>\d+)?$', InvitationView.as_view(), name='invitation'),
    path('admin/login', LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('admin/', login_required(AdminView.as_view()), name='admin_main'),
]
