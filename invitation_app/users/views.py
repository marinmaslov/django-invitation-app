from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm

from django.views.generic import TemplateView

from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('/u/' + username)
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})






class UserProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['invitations'] = "Invitation.objects.all()"
        return context



