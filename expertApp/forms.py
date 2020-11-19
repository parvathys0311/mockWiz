from django.forms import ModelForm, TextInput, EmailInput, Select, ModelChoiceField, URLInput, FileInput, Textarea

from pagesApp.models import Function
from .models import Expert
from django import forms


class Expertform(ModelForm):
    expertiseFunction = ModelChoiceField(Function.objects.all(), empty_label="Select your desired role")
    class Meta:
        model=Expert
        fields=('firstName','email','expertiseFunction','lastname','linkedInUrl','yearsInterviewedFor','approved',
                'phoneNumber','jobTitle','organization','imageProfile','city','country','summary','published','expertise'
               )

        widgets = {
            'firstName':TextInput(attrs={'id':'Name', 'placeholder':'First Name', 'class':'ex-input'}),
            'email': EmailInput(attrs={'id':'Email', 'placeholder':'Email Address', 'class':'ex-input'}),
            'expertiseFunction': Select(attrs={'id': 'Function', 'class': 'ex-input'}),
            'lastname': TextInput(attrs={'id': 'LastName', 'placeholder': 'Last Name', 'class': 'ex-input'}),
            'linkedInUrl': URLInput(attrs={'id': 'linkedInUrl', 'placeholder': 'LinkedIn Profile Url', 'class': 'ex-input'}),
            'yearsInterviewedFor': Select(attrs={'id': 'yearsInterviewed', 'class': 'ex-input'}),
            'approved': Select(attrs={'id': 'approved', 'class': 'ex-input'}),
            'phoneNumber': TextInput(attrs={'id':'phoneNo', 'placeholder':'Phone Number', 'class':'ex-input'}),
            'jobTitle': TextInput(attrs={'id':'job', 'placeholder':'Title', 'class':'ex-input'}),
            'organization': TextInput(attrs={'id':'organization', 'placeholder':'Organization', 'class':'ex-input'}),
            # 'imageProfile': FileInput(attrs={'class': 'ex-input','id':'imgEx'}),
            'city': TextInput(attrs={'id': 'City', 'placeholder': 'City', 'class': 'ex-input'}),
            'country': TextInput(attrs={'id': 'Country', 'placeholder': 'Country', 'class': 'ex-input'}),
            'expertise': Textarea(attrs={'id': 'exp', 'placeholder': 'Enter keywords related to your expertise, for ex, Project Management, Quality Assurance', 'class':'ex-input'}),
            'summary': Textarea(attrs={'id': 'Summary', 'placeholder': 'Tell Us about you in few words', 'class': 'ex-input'}),
        }
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     for instance in Expert.objects.all():
    #         if instance.email == email:
    #             raise forms.ValidationError("Email already exists. Looks like you have made an enquiry already. Our team will get back to you soon.")
    #     return email

    def clean_email(self):
        email = self.cleaned_data['email']
        if self.instance and self.instance.pk:
            # this condition is true in case of editing the existing form data
            return email
        elif (Expert.objects.filter(email=email).exists()):
            # this condition is true while registering a new form record
            raise forms.ValidationError('Email Error')
        return email