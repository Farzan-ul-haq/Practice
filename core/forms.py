from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class UserLoginform(ModelForm):
    class Meta:
        model=User
        fields=['email','password']