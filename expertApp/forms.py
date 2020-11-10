from django.forms import ModelForm, TextInput, EmailInput, Select, ModelChoiceField, URLInput

from pagesApp.models import Function
from .models import Expert
from django import forms


class Expertform(ModelForm):
    expertiseFunction = ModelChoiceField(Function.objects.all(), empty_label="Select your desired role")
    class Meta:
        model=Expert
        fields=('firstName','email','expertiseFunction','lastname','linkedInUrl','yearsInterviewedFor','approved'
               )

        widgets = {
            'firstName':TextInput(attrs={'id':'Name', 'placeholder':'First Name', 'class':'ex-input'}),
            'email': EmailInput(attrs={'id':'Email', 'placeholder':'Email Address', 'class':'ex-input'}),
            'expertiseFunction': Select(attrs={'id': 'Function', 'class': 'ex-input'}),
            'lastname': TextInput(attrs={'id': 'LastName', 'placeholder': 'Last Name', 'class': 'ex-input'}),
            'linkedInUrl': URLInput(attrs={'id': 'linkedInUrl', 'placeholder': 'LinkedIn Profile Url', 'class': 'ex-input'}),
            'yearsInterviewedFor': Select(attrs={'id': 'yearsInterviewed', 'class': 'ex-input'}),
            'approved': Select(attrs={'id': 'approved', 'class': 'ex-input'})
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        for instance in Expert.objects.all():
            if instance.email == email:
                raise forms.ValidationError("Email already exists. Looks like you have made an enquiry already. Our team will get back to you soon.")
        return email