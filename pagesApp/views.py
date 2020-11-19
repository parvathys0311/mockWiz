import os
import uuid

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
    # home page has 2 forms - Candidateform & Experform
    forms_new = {}
    formCdd = Candidateform()
    formExp = Expertform()
    print(formExp)
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
                try:
                    send_mail('Cdd Form Submission', 'Here is the message.', 'parvathys0311@gmail.com',
                          ['parvathys0387@gmail.com'],
                          fail_silently=False)
                except Exception:
                    pass
                return redirect('home')

        elif 'submit-exp' in request.POST:  # expert form submission
            formExp = Expertform(request.POST)
            print(formExp)
            if formExp.is_valid():
                data = formExp.cleaned_data
                # save form
                formExp.save()
                # display success message for user
                messages.success(request,'Expert form is submitted successfully')

                createdExpertEmail = formExp['email'].value()
                createdExpert = Expert.objects.filter(email=createdExpertEmail)

                # send confirmation email to expert on successful form submission
                name = createdExpert[0].firstName
                email = createdExpert[0].email
                send_mail('Welcome to MockWiz', f'Hi {name}, thanks for registering with us.We will get back to you soon.', 'parvathys0311@gmail.com',
                          [email],fail_silently=False)

                # send an email to admin to approve the expert profile
                createdExpertSlug = createdExpert[0].slug
                link = "http://127.0.0.1:8000/approve/" + str(createdExpertSlug)
                send_mail('Approve the expert Profile submitted', f'Here is the URL -- {link} to approve', 'parvathys0311@gmail.com',
                          ['parvathys0387@gmail.com'],
                          fail_silently=False)
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
        if form.is_valid():
            updatedForm = form.save(commit=False)
            updatedForm.save()

            # retrieve expert info
            name = expert.firstName
            email = expert.email

            if(expert.approved == "N"):
                # (not approved) send email to expert -- WAITLIST status
                send_mail('Member Status',
                          f'Hi {name}, You are on waitinglist',
                          'parvathys0311@gmail.com',
                          [email], fail_silently=False)
            else:
                # (approved) send email to expert -- provide link to add more info to their profile

                random = randomidgenerator() # create a random id to add to url - for security
                link = f"http://127.0.0.1:8000/edit/{random}/" + str(expert.slug)
                send_mail('Member Status',
                          f'Hi {name}, We are excited to inform that your application is approved. Next step is to build a portfolio for you with MockWiz. Give us more info about you and we shall do the rest. Update your profile here - {link} .',
                          'parvathys0311@gmail.com',
                          [email], fail_silently=False)
            params = {
                'form': updatedForm,
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

def editProfile_Ex(request, randomId, slug_text):
    expert = Expert.objects.filter(slug=slug_text)
    if expert.exists():
        expert = expert.first()
    else:
        return HttpResponse("<h1>Page not found</h1>")
    # print(expert.approved)
    if request.method == 'POST':
        form = Expertform(request.POST, request.FILES or None, instance=expert)
        # print(form)
        if form.is_valid():
            updatedForm = form.save(commit=False)
            try:
                updatedForm.imageProfile = request.FILES['imageProfile']
            except Exception:
                pass

            if updatedForm.imageProfile:
                updatedForm.save()
            else:
                print("no image")
                params = {
                            'form': form,
                            'message': 'Please upload a picture'
                        }
                return render(request, 'pages/additionalInfoExpert.html', params)

            # except:
            #     params = {
            #         'form': form,
            #         'message': 'Please upload a picture'
            #     }
            #     return render(request, 'pages/additionalInfoExpert.html', params)

            # submission success message
            # messages.success(request,
            #                  'Successful submission')

            # retrieve expert info
            senderEmail = expert.email
            name = expert.firstName
            # create a link for profile page of the expert
            link = "http://127.0.0.1:8000/expert/" + str(expert.slug)
            editLink = f"http://127.0.0.1:8000/edit/{randomId}/" + str(expert.slug)

            # send email to expert with link to their profile page
            email = EmailMessage(
                'Your MockWiz profile',
                f'Hi {name}, View the profile you created with MockWiz -- {link} .MockWiz is happy to partner with you. If you wish to update your profile, you can do via {editLink}',
                'parvathys0311@gmail.com',
                [senderEmail, 'parvathy.labwork@gmail.com'],
                ['parvathys0311@gmail.com']
            )
            email.send(fail_silently=False)

            # params = {
            #     'form': updatedForm,
            # }
            # return render(request, "pages/additionalInfoExpert.html", params)

            # redirect expert to their profile page
            # return redirect(link)

            return render(request,"pages/congratulations.html")
        else:
            params = {
                'form': form,
                'message':'Oops.Something went wrong. Please try again'
            }
            return render(request, 'pages/additionalInfoExpert.html', params)
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

def randomidgenerator():
    s = str(uuid.uuid4())
    print(s)
    firstNineChars = s.split("-",1)
    print(firstNineChars)
    randomString = "C" + str(firstNineChars[0])
    return randomString

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