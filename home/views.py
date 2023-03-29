from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.core.mail import send_mail #I will get this to send an email with how many new applications there have been a day
from .models import Applications, CustomUser

def index(request):
    #testText = Applications.objects.createApplicationQuestion(request.user, "TEST", "TEST")
    
    return render(request, "test.html") #loads the test template onto the session

def adminview(request):
    if request.user.is_staff:
        usercount = 0
        applicationinprogcount= 0
        completedapplications = 0
        unreadapplications = 0
        userlist = CustomUser.objects.filter(is_staff = False)
        applicationlist = Applications.objects.all()
        applicationinprogcount = applicationlist.filter(complete = False).__len__()
        applicationinprogcount = str(applicationinprogcount)
        completedapplications = applicationlist.filter(complete = True).__len__()
        completedapplications = str(completedapplications)
        unreadapplications = applicationlist.filter(read = False, complete = True).__len__()
        unreadapplications = str(unreadapplications)
        usercount = userlist.__len__()
        usercount = str(usercount)
        return render(request, "index.html", locals())