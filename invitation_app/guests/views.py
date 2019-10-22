from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from guests.models import Invitation, Guest
from .forms import SlugForm


#def get_invitations(request):


def get_invitations(request):
    if request.method == 'POST':
        form = SlugForm(request.POST)
        if form.is_valid():
            slug = form.cleaned_data['slug']
            invitation = Invitation.objects.filter(slug=slug).first()
            guest = Guest.objects.filter(invitation = invitation.id).first()
            context = {
                'slug': invitation.slug,
                'created': invitation.created,
                'confirmed': invitation.confirmed,
                'isFamily': invitation.isFamily,
                'guest': guest
            }
            return render(request, 'guests/templates/invitation.html', context)

    form = SlugForm()
    return render(request, 'guests/templates/slug.html', {'form': form})



#class GuestView(TemplateView):
