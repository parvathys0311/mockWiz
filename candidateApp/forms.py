from django.core.validators import validate_email
from django.forms import ModelForm, TextInput, EmailInput, Select, ModelChoiceField

from pagesApp.models import Role
from .models import Candidate

from django import forms

class Candidateform(ModelForm):
    interestedRole = ModelChoiceField(Role.objects.all(),empty_label="------ Select ------")
    class Meta:
        model=Candidate
        fields=('firstName','email','interestedRole')

        widgets = {
            'firstName':TextInput(attrs={'class': 'form-control', 'id':'Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id':'Email'}),
            'interestedRole': Select(attrs={'class': 'form_control', 'id': 'Role'}),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        for instance in Candidate.objects.all():
            if instance.email == email:
                raise forms.ValidationError("Email already exists. Looks like you have made an enquiry already. Our team will get back to you soon.")

        # if not (email):
        #     raise forms.ValidationError(
        #     "You must enter either a phone number or an email, or both.")

        # try:
        #     mt = validate_email(email)
        # except:
        #     return forms.ValidationError("Email is not in correct format")
        # return email
    # def clean_email(self):