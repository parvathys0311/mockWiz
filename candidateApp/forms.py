from itertools import chain

from django.core.validators import validate_email
from django.forms import ModelForm, TextInput, EmailInput, Select, ModelChoiceField
from django.forms.utils import flatatt
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from pagesApp.models import Role
from .models import Candidate

from django import forms


class Candidateform(ModelForm):
    interestedRole = ModelChoiceField(Role.objects.all(),empty_label="Select your desired role")
    class Meta:
        model=Candidate
        fields=('firstName','email','interestedRole')

        widgets = {
            'firstName':TextInput(attrs={'id':'Name', 'placeholder':'First Name'}),
            'email': EmailInput(attrs={'id':'Email','placeholder':'Email Address'}),
            'interestedRole': Select(attrs={'class': 'selectCdd', 'id': 'role'}),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        for instance in Candidate.objects.all():
            if instance.email == email:
                raise forms.ValidationError("Email already exists. Looks like you have made an enquiry already. Our team will get back to you soon.")
        return email

        # if not (email):
        #     raise forms.ValidationError(
        #     "You must enter either a phone number or an email, or both.")

        # try:
        #     mt = validate_email(email)
        # except:
        #     return forms.ValidationError("Email is not in correct format")
