from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

from django.utils.crypto import get_random_string
import datetime

from .models import Board, Invitation, Escort

from .forms import SlugForm, NewInvitation

class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = SlugForm()
        return render(request, "base/index.html", {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = SlugForm(request.POST)
            if form.is_valid():
                slug = form.cleaned_data['slug']
                
                if Invitation.objects.filter(slug=slug).exists():
                    invitation = Invitation.objects.filter(slug=slug).first()
                    context = {
                        'slug': invitation.slug,
                        'created': invitation.created,
                        'confirmed': invitation.confirmed,
                        'multiple_escort': invitation.multiple_escort,
                        'name': invitation.name,
                        'surname': invitation.surname,
                    }
                    return render(request, "base/invitation.html", context)
                else:
                    return render(request, "base/index.html", {'form': form})



class UserProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['invitations'] = "Invitation.objects.all()"
        return context

