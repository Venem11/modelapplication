from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.core.mail import send_mail #I will get this to send an email with how many new applications there have been a day
from .models import ApplicationQuestionText

def index(request):
    testText = ApplicationQuestionText.objects.createApplicationQuestion(request.user, "TEST", "TEST")
    
    return render(request, "test.html") #loads the test template onto the session