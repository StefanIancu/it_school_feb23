from django import forms
from .models import Dweet

class DweetForm(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = Dweet
        exclude = ("user", )