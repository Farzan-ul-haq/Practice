from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate,login as dj_login,logout
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')



def register(request):
    returnrender(request,'register.html')