from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required

from .views import register#, UserProfileView

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    # Authentication urls
    path('a/register/', register, name='register'),
    path('a/login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('a/logout/', LogoutView.as_view(template_name='auth/logout.html'), name='logout'),

    path('a/password/reset/', PasswordResetView.as_view(template_name='auth/password/reset/reset.html'), name='password_reset'),
    path('a/password/reset/done/', PasswordResetDoneView.as_view(template_name='auth/password/reset/done.html'), name='password_reset_done'),
    path('a/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='auth/password/reset/confirm.html'), name='password_reset_confirm'),
    path('a/password/reset/complete/', PasswordResetCompleteView.as_view(template_name='auth/password/reset/complete.html'), name='password_reset_complete'),

    path('a/password/change/', PasswordChangeView.as_view(template_name='auth/password/change/change.html'), name='password_change'),
    path('a/password/change/done', PasswordChangeDoneView.as_view(template_name='auth/password/change/done.html'), name='password_change_done'),

    #path('u/profile/<slug:username>/', login_required(UserProfileView.as_view()), name='profile'),
]