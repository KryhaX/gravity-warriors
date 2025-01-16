from django.forms import ModelForm

from .models import Dips, Pull_ups

class DipsForm(ModelForm):
    class Meta:
        model = Dips
        exclude = ['rank']

class Pull_upsForm(ModelForm):
    class Meta:
        model = Pull_ups
        exclude = ['rank']

