from django import forms

class SlugForm(forms.Form):
    slug = forms.CharField(max_length=8)

# Kreira novog Gosta i Invite te ih spaja
class NewInvitation(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    phone = forms.IntegerField()
    email = forms.EmailField()
    isFamily = forms.BooleanField()