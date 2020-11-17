import os

from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from candidateApp.forms import Candidateform
from candidateApp.models import Candidate
from expertApp.forms import Expertform
from expertApp.models import Expert


def home(request):
    forms_new = {}
    formCdd = Candidateform()
    formExp = Expertform()
    if request.method == 'POST':  # POST action in homepage
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
                # send_mail('Cdd Form Submission', 'Here is the message.', 'parvathys0311@gmail.com',
                #           ['parvathys0387@gmail.com'],
                #           fail_silently=False)
                return redirect('home')

        elif 'submit-exp' in request.POST:  # expert form submission
            formExp = Expertform(request.POST)
            if formExp.is_valid():
                data = formExp.cleaned_data
                # save form
                formExp.save()
                # display message for user
                messages.success(request,
                                 'Expert form message')
                # send confirmation email
                createdExpertEmail = formExp['email'].value()
                createdExpert = Expert.objects.filter(email=createdExpertEmail)
                createdExpertSlug = createdExpert[0].slug
                link = "http://127.0.0.1:8000/approve/" + str(createdExpertSlug)
                print(link)

                # send_mail('Expert form submission', f'Here is the URL -- {link}', 'parvathys0311@gmail.com',
                #           ['parvathys0387@gmail.com'],
                #           fail_silently=False)
                return redirect('home')
    forms_new['formcd'] = formCdd
    forms_new['formex'] = formExp
    return render(request,'pages/index.html',{'form': forms_new})

def approve(request, slug_text):
    expert = Expert.objects.filter(slug=slug_text)
    if expert.exists():
        expert = expert.first()
    else:
        return HttpResponse("<h1>Page not found</h1>")
    # print(expert.approved)
    if request.method == 'POST':
        form = Expertform(request.POST, instance=expert)
        print(form)
        if form.is_valid():
            updatedForm = form.save(commit=False)
            updatedForm.save()

            if(expert.approved == "N"):
                # send email to expert -- WAITLIST
                print("Its no")
            else:
                # send email to expert -- MORE INFO LINK
                print("It is a Yes")
            params = {
                'form': form,
                'message': "Successfully entered",
            }
            return render(request, "pages/approve.html", params)
        else:
            print("Error in Saving")
    else:
        form = Expertform(instance=expert)
        params = {
            'form': form,
        }
        return render(request, "pages/approve.html",params)

def editProfile_Ex(request, slug_text):
    expert = Expert.objects.filter(slug=slug_text)
    if expert.exists():
        expert = expert.first()
    else:
        return HttpResponse("<h1>Page not found</h1>")
    # print(expert.approved)
    if request.method == 'POST':
        form = Expertform(request.POST, instance=expert)
        # print(form)
        if form.is_valid():
            updatedForm = form.save(commit=False)
            updatedForm.save()
            link = "http://127.0.0.1:8000/expert/" + str(expert.slug)
            print(link)
            email = EmailMessage(
                'Your MockWiz profile',
                f'Hi User, here is the profile you created for yourself with MockWiz -- {link}.MockWiz is happy to partner with you.',
                'parvathys0311@gmail.com',
                ['parvathys0387@gmail.com', 'parvathy.labwork@gmail.com'],
                ['parvathys0311@gmail.com']
            )
            email.send(fail_silently=False)
            params = {
                'form': form,
                'message': "Successfully entered",
            }
            return render(request, "pages/additionalInfoExpert.html", params)
    else:
        form = Expertform(instance=expert)
        params = {
            'form': form,
        }
        return render(request,'pages/additionalInfoExpert.html', params)

def expertProfile(request,slug_text):
    expert = Expert.objects.filter(slug=slug_text)
    if expert.exists():
        expert = expert.first()
    else:
        return HttpResponse("<h1>Page not found</h1>")
    params = {
        'expert': expert
    }
    return render(request, 'pages/expertProfile.html',params)

def test(request):
    # forms_new = {}
    # form1 = Candidateform()
    # form2 = Expertform()
    # if request.method == 'POST':        # POST action in homepage
    #     if 'submit-cdd' in request.POST: # candidate form submission
    #         form1 = Candidateform(request.POST)
    #         if form1.is_valid():
    #             data = form1.cleaned_data
    #             # save form
    #             form1.save()
    #             # display message for user
    #             messages.success(request,
    #                              ': You have successfully submitted your details. Our team will get back to you soon.')
    #             # send confirmation email
    #             send_mail('Subject here', 'Here is the message.', 'parvathys0387@gmail.com',
    #                       ['parvathys0311@gmail.com'],
    #                       fail_silently=False)
    #             return redirect('test')
    #
    #     elif 'submit-exp' in request.POST:   # expert form submission
    #         form2 = Expertform(request.POST)
    #         if form2.is_valid():
    #             data = form2.cleaned_data
    #             # save form
    #             form2.save()
    #             # display message for user
    #             messages.success(request, ': You have successfully submitted your details. Our team will get back to you soon.')
    #             # send confirmation email
    #             send_mail('Subject here', 'Here is the message.', ['parvathy.labwork@zohomail.com'],
    #                       ['parvathys0311@gmail.com'],
    #                       fail_silently=False)
    #             return redirect('test')
    #
    #     # # GMAIL setup
    #     # email_client = (
    #     #     'Welcome to MockWiz', 'Hello ' + data['firstName'] + ",\n\nLet's get started", 'parvathy.labwork@gmail.com',
    #     #     ['parvathys0311@gmail.com']
    #     # )
    #     # email_internal = (
    #     #     'Submission', 'Hello Admin, A submission has been made', 'parvathy.labwork@gmail.com',
    #     #     ['parvathy.labwork@gmail.com']
    #     # )
    #     # send_mass_mail((email_client, email_internal), fail_silently=False)
    #
    # # messages.error(request, form1.errors)
    # # messages.error(request, form2.errors)
    # forms_new['formcd'] = form1
    # forms_new['formex'] = form2
    # {'form': forms_new}
    return render(request, "pages/test.html")

def sendgridtest(request):
    send_mail('Subject here', 'Here is the message.', 'parvathys0387@gmail.com',
              ['parvathys0311@gmail.com'],
              fail_silently=False)
    return redirect(home)