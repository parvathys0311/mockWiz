from django.forms import ModelForm, TextInput, EmailInput, Select

from .models import Candidate

from django import forms

class Candidateform(ModelForm):
    class Meta:
        model=Candidate
        fields=('candidateId','firstName','email','interestedRole'
               )

        widgets = {
            'firstName':TextInput(attrs={'class': 'form-control', 'id':'Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id':'Email'}),
            'interestedRole': Select(attrs={'class': 'form_control', 'id': 'Role'}),
        }