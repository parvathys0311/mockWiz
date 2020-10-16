from django.forms import ModelForm, TextInput, EmailInput, Select

from .models import Expert
from django import forms


class Expertform(ModelForm):
    class Meta:
        model=Expert
        fields=('expertId','firstName','email','expertiseFunction'
               )

        widgets = {
            'firstName':TextInput(attrs={'class': 'form-control', 'id':'Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id':'Email'}),
            'expertiseFunction': Select(attrs={'class': 'form_control', 'id': 'Function'}),
        }