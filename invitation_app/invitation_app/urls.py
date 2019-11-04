from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', include('invitations.urls')),
    path('', include('users.urls')),

    #path('admin/login/', LoginView.as_view(template_name='templates/login.html'), name='login'),
    #path('admin/', LoginView.as_view(template_name='templates/login.html'), name='login'),


    # SREDIT
    #path('admin/', LoginView.as_view(template_name='templates/login.html'), name='login'),

    #path('admin/login/', LoginView.as_view(template_name='templates/login.html'), name='login'),
    #path('admin/logout/', LogoutView.as_view(template_name='templates/logout.html'), name='logout'),

    #path('admin/password_change/', PasswordChangeView.as_view(template_name='common_templates/password_change_form.html'), name='password_change'),
    #path('admin/password_change_done/', PasswordChangeDoneView.as_view(template_name='common_templates/password_change_done.html'), name='password_change_done'),


    path('superadmin/', admin.site.urls),


]
