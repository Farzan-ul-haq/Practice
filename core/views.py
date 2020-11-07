from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login as dj_login,logout
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
# Create your views here.

def index(request):
    return render(request,'index.html',{'user':request.user})

#we are using default django login page thats why we didnt create its view
#but logout function is required to create
def logout(request):
    return redirect('/login/')

@transaction.atomic
def register(request):
    form=UserSignUpForm()
    if request.method == 'POST':
        print("================")
        form=UserSignUpForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data['password1']
            email=form.cleaned_data['email']
            form.save()
            print(email,password)
            user=authenticate(request,username=email,password=password)
            print(user)
            if user is not None:
                dj_login(request,user)
                return redirect('/')
        
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})