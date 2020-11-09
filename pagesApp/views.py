import os

from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.shortcuts import render, redirect

# Create your views here.
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from candidateApp.forms import Candidateform
from candidateApp.models import Candidate
from expertApp.forms import Expertform

def home(request):
    forms_new = {}
    formCdd = Candidateform()
    formExp = Expertform()
    if request.method == 'POST':  # POST action in homepage
        print("POST")
        if 'submit-cdd' in request.POST:  # candidate form submission
            formCdd = Candidateform(request.POST)
            if formCdd.is_valid():
                data = formCdd.cleaned_data
                # save form
                formCdd.save()
                # display message for user
                messages.success(request,
                                 'You have successfully submitted your details. Our team will get back to you soon.')
                # send confirmation email
                send_mail('Cdd Form Submission', 'Here is the message.', 'parvathys0387@gmail.com',
                          ['parvathys0311@gmail.com'],
                          fail_silently=False)
                return redirect('home')

        elif 'submit-exp' in request.POST:  # expert form submission
            print("yes")
            formExp = Expertform(request.POST)
            if formExp.is_valid():
                print("valid")
                data = formExp.cleaned_data
                # save form
                formExp.save()
                # display message for user
                messages.success(request,
                                 'Expert form message')
                # send confirmation email
                send_mail('Expert form submission', 'Here is the message.', 'parvathys0387@gmail.com',
                          ['parvathys0311@gmail.com'],
                          fail_silently=False)
                return redirect('home')
    forms_new['formcd'] = formCdd
    forms_new['formex'] = formExp
    return render(request,'pages/index.html',{'form': forms_new})

def test(request):
    forms_new = {}
    form1 = Candidateform()
    form2 = Expertform()
    if request.method == 'POST':        # POST action in homepage
        if 'submit-cdd' in request.POST: # candidate form submission
            form1 = Candidateform(request.POST)
            if form1.is_valid():
                data = form1.cleaned_data
                # save form
                form1.save()
                # display message for user
                messages.success(request,
                                 ': You have successfully submitted your details. Our team will get back to you soon.')
                # send confirmation email
                send_mail('Subject here', 'Here is the message.', 'parvathys0387@gmail.com',
                          ['parvathys0311@gmail.com'],
                          fail_silently=False)
                return redirect('test')

        elif 'submit-exp' in request.POST:   # expert form submission
            form2 = Expertform(request.POST)
            if form2.is_valid():
                data = form2.cleaned_data
                # save form
                form2.save()
                # display message for user
                messages.success(request, ': You have successfully submitted your details. Our team will get back to you soon.')
                # send confirmation email
                send_mail('Subject here', 'Here is the message.', ['parvathy.labwork@zohomail.com'],
                          ['parvathys0311@gmail.com'],
                          fail_silently=False)
                return redirect('test')

        # # GMAIL setup
        # email_client = (
        #     'Welcome to MockWiz', 'Hello ' + data['firstName'] + ",\n\nLet's get started", 'parvathy.labwork@gmail.com',
        #     ['parvathys0311@gmail.com']
        # )
        # email_internal = (
        #     'Submission', 'Hello Admin, A submission has been made', 'parvathy.labwork@gmail.com',
        #     ['parvathy.labwork@gmail.com']
        # )
        # send_mass_mail((email_client, email_internal), fail_silently=False)

    # messages.error(request, form1.errors)
    # messages.error(request, form2.errors)
    forms_new['formcd'] = form1
    forms_new['formex'] = form2
    return render(request, "pages/test.html",{'form': forms_new})

def sendgridtest(request):

    send_mail('Subject here', 'Here is the message.', 'parvathys0387@gmail.com',
              ['parvathys0311@gmail.com'],
              fail_silently=False)
    return redirect(home)