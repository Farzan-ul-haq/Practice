from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(UserLoginForm,self).__init__(*args,**kwargs)
    username=forms.EmailField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'','id':'id_email'}
    ))
    password=forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'','id':'id_password_edited'}
    ))
# class UserLoginform(ModelForm):
#     class Meta:
#         model=User
#         fields=['email','password']