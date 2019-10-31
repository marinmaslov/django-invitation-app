from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

from django.utils.crypto import get_random_string
import datetime

from invitations.models import Board, Invitation, Escort
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




class MainView(View):
    def get(self, request, *args, **kwargs):
        form = SlugForm()
        return render(request, 'invitations/templates/index.html', {'form': form})

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
                return render(request, 'invitations/templates/invitation.html', context)





# NADOGRADITI TAKO DA IMA NEKAKVI DASHBOARD S BOARDOVIMA I INFORMACIJAMA I ONJIMA, KAO I INFORMACIJE O PROFILU TRENUTNOG KORISNIKA
class AdminView(TemplateView):
    template_name = "admin/admin.html"

    def get_context_data(self, **kwargs):
        context = super(AdminView, self).get_context_data(**kwargs)
        context['boards'] = Board.objects.all()
        context['invitations'] = Invitation.objects.all()
        context['escorts'] = Escort.objects.all()
        return context


    def post(self, request):
        action = request.POST.get('action', '')

        if action == "createNewInvitation":
            form = NewInvitation()
            return render(request, 'admin/new_invitation.html', {'form': form})

        elif action == "submitInvitation":
            form = NewInvitation(request.POST)

            return HttpResponse(render(request, 'admin/new_invitation.html', {'form': form}))

        else:
            return HttpResponse(status=400, content="No service available for action requested")


        """ action = request.POST.get('action', '')

        if action == "createNewInvitation":
            form = NewInvitation()
            return render(request, 'admin/new_invitation.html', {'form': form})

        elif action == "submitInvitation":
            form = NewInvitation(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                surname = form.cleaned_data['surname']
                phone = int(form.cleaned_data['phone'])
                email = form.cleaned_data['email']
                invitation = Invitation(slug=get_random_string(length=8), created=datetime.datetime.now(), confirmed=False)
                invitation.save()
                guest = Guest(name=name, surname=surname, phone=phone, email=email, invitation_id=invitation.id)
                guest.save()
        """


class AdminBoardView(TemplateView):
    template_name = "admin/board.html"

    def get_context_data(self, **kwargs):
        context = super(AdminBoardView, self).get_context_data(**kwargs)
        context['boards'] = Board.objects.all()
        context['invitations'] = Invitation.objects.all()
        context['escorts'] = Escort.objects.all()
        return context


    def post(self, request):
        action = request.POST.get('action', '')

        if action == "createNewInvitation":
            form = NewInvitation()
            return render(request, 'admin/new_invitation.html', {'form': form})

        elif action == "submitInvitation":
            form = NewInvitation(request.POST)

            return HttpResponse(render(request, 'admin/new_invitation.html', {'form': form}))

        else:
            return HttpResponse(status=400, content="No service available for action requested")


class AdminInvitationView(TemplateView):
    template_name = "admin/invitation.html"

    def get_context_data(self, **kwargs):

        context = super(AdminInvitationView, self).get_context_data(**kwargs)

        # Cycle_id is a key. requested_cycle will be a value from key-value pair
        requested_invitation = kwargs["invitation_id"]


        if requested_invitation is None:
            # Order cycles by id and show first of the list
            invitation = Invitation.objects.order_by('-id').first()
        else:
            # Filter cycles by id of the cycle requested and show first of the list
            invitation = Invitation.objects.filter(id=int(requested_invitation)).first()

        context['invitation'] = invitation
        # Upgrade Logical Area will be fetched by template (Key headers only)
        context['escorts'] = Escort.objects.filter(invitation_id=invitation.id)

        return context
