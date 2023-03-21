from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.core.mail import send_mail


def index(request):
    return render(request, "test.html")