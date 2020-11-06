from django.shortcuts import render
from .forms import UserLoginform
from django.contrib.auth import authenticate,login as dj_login,logout
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    form=UserLoginform()
    if request.method == 'POST':
        form=UserLoginform(request.POST)
        print(form)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user=authenticate(request,email=email,password=password)
            print(user)
            if user is not None:
                dj_login(request,user)
                return redirect('/')
            else:
                return render(request,'login.html',{'error':'Incorrect Id Or'})
            #user=form.save()
            #log=authenticate(request,email=)


    return render(request,'login.html',{'form':form})

def register(request):
    returnrender(request,'register.html')