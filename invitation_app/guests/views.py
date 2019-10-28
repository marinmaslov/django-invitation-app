from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

from django.utils.crypto import get_random_string
import datetime

from guests.models import Invitation, Guest, Escort
from .forms import SlugForm, NewInvitation


'''
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
'''




class GuestView(View):
    def get(self, request, *args, **kwargs):
        form = SlugForm()
        return render(request, 'guests/templates/index.html', {'form': form})

    def post(self, request, *args, **kwargs):
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


class AdminView(TemplateView):
    template_name = "admin/admin.html"

    def get_context_data(self, **kwargs):
        context = super(AdminView, self).get_context_data(**kwargs)
        context['invitations'] = Invitation.objects.all()
        context['guests'] = Guest.objects.all()
        context['escorts'] = Escort.objects.all()
        return context

    @staticmethod
    def post(request):
        action = request.POST.get('action', '')

        if action == "createNewInvitation":
            form = NewInvitation()
            return render(request, 'admin/new_invitation.html', {'form': form})

        elif action == "subminInvitation":
            print("KAKAO: "+request)
            form = NewInvitation(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                surname = form.cleaned_data['surname']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                isFamily = form.cleaned_data['isFamily']
                invitation = Invitation(slug=get_random_string(length=8), created=datetime.datetime.now(), confirmed=False, isFamily=isFamily)
                print("KAKAO: "+invitation)
                invitation.save()
                guest = Guest(name=name, surname=surname, phone=phone, email=email, invitation_id=invitation.id)
                guest.save()
                return "MRKVA"