from django.forms import ModelForm
from django.forms import ModelForm
from django import forms
from .models import User,Profile
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.utils.safestring import mark_safe
from string import Template


#updating Image field


class UserLoginForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(UserLoginForm,self).__init__(*args,**kwargs)
    username=forms.EmailField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'','id':'id_email'}
    ))
    password=forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'','id':'id_password_edited'}
    ))

    # def save(self):
    #     user=authenticate(username=self.email,password=self.password)
    #     if user is not None:
    #         return user
    #     else:
    #         return 'No User found'

# class UserLoginform(ModelForm):
#     class Meta:
#         model=User
#         fields=['email','password']


class UserSignUpForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(UserSignUpForm,self).__init__(*args,**kwargs)

    email=forms.EmailField(widget=forms.TextInput(
        attrs={'class':'form-control','id':'id_email','placeholder':'Email...'}
    ))
    name=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','id':'id_name','placeholder':'Name...'}
    ))
    password1=forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','id':'id_email','placeholder':'Password...'}
    ))
    password2=forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','id':'id_email','placeholder':'Password...'}
    ))
    class Meta:
        model=User
        fields=['email','name','password1','password2']
    # def save(self):
    #     username=forms.cleaned_data['username']
    #     name=forms.cleaned_data['name']
    #     password1=forms.cleaned_data['password1']
    #     password2=forms.cleaned_data['password2']
    #     print(name,email,password1,password2)
    #     self.save()

class ProfileUpdateForm(ModelForm):
    class Meta:
        model=Profile
        fields=['phone','image']