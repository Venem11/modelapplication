from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    RealName = models.CharField(max_length= 50)
    PornName = models.CharField(max_length= 50)
    DateofBirth = models.DateField(default= timezone.now)
    #pictures = models.FileField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class ApplicationQuestionText(models.Model):
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE, default= 0)
    question = models.CharField(max_length= 40)
    answer = models.CharField(max_length= 200)
class ApplicationQuestionTrueOrFalse(models.Model):
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE, default= 0)
    question = models.CharField(max_length= 40)
    answer = models.BooleanField(default= False)
