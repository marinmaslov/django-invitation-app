from django import forms

class SlugForm(forms.Form):
    slug = forms.CharField(max_length=8)
