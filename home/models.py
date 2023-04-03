from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin): #THIS is the model that is used for registering users
    email = models.EmailField(_("email address"), unique=True) #makes sure that the email users sign up with is what is used to login, this is further reinforced further down
    RealName = models.CharField(max_length= 50)
    PornName = models.CharField(max_length= 50)
    DateofBirth = models.DateField(default= timezone.now)
    profileImage = models.ImageField(upload_to='profilePic', default='ApplyToModelLogo.png')#This stores 1 picture of the user
    is_staff = models.BooleanField(default=False) #This grants differant permissions if this is ticked
    bio = models.CharField(max_length= 1000, default= 'Please type your bio here')
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"#as mentioned on the email field this reinforces that the users sign in using their email
    REQUIRED_FIELDS = ['RealName', 'DateofBirth']

    objects = CustomUserManager()

    def __str__(self):
        return self.email #if users are referanced outside of this function then the email field is going to be what identifies it 
    

class Event(models.Model):
    EventName = models.CharField(max_length= 30, default= 'Please enter a title for your event')
    EventDetails = models.CharField(max_length= 600, default= 'Please enter a description for your event')
    EventStartDate = models.DateTimeField(default= timezone.now)
    EventEndDate = models.DateTimeField(default= timezone.now)

#ALL FUNCTIONS BELOW ARE SUBJECT TO CHANGE AS THESE ARE THE APPLICATION QUESTIONS
class ApplicationManager(models.Manager):
    def createApplicationQuestion(self, user, question1ans, question2ans):
        applicationquestion = self.create(user=user, question1ans= question1ans, question2ans=question2ans)
        return applicationquestion
    
class Applications(models.Model):
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE, default= 0)
    question1ans = models.CharField(max_length= 40)
    question2ans = models.CharField(max_length= 200)
    read = models.BooleanField(default= False)
    complete = models.BooleanField(default= False)
    objects = ApplicationManager()

    def __str__(self):
        return self.user.RealName + "'s Application"

