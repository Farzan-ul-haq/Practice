from django.shortcuts import render,redirect,HttpResponse
from .forms import *

from django.contrib.auth import authenticate,login as dj_login,logout
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from . import signals
# Create your views here.   

def index(request):
    # try:
    print(request.session['_auth_user_id'],request.user)
    profile=Profile.objects.get(user=request.user)
    post=Post.objects.get_post(profile)
    print(post)
    #signals.notification.send(sender=None,request=request,user=request.user.name)
    return render(request,'index.html',{'profile':profile,'post':post})
                                    
    # except Exception as e:
    #     print(f'Error\t{e}')
    #     print('Not Working')
    #     return redirect('/login/')
    # else:
    #     return redirect('/login/')
    # print(request.user.is_authenticated)
    # if request.user.is_authenticated:
    #     profile=Profile.objects.get(user=request.user)
    
    #     print(profile)
    #     post=Post.objects.get(author=profile)
    # #signals.notification.send(sender=None,request=request,user=request.user.name)
    #     return render(request,'index.html',{'profile':profile,
    #                                     'post':post})
    # else:
    #     return redirect('/login/')

#we are using default django login page thats why we didnt create its view
#but logout function is required to create

def handlelogout(request):
    logout(request)
    return redirect('/login/')

@transaction.atomic
def register(request):
    form=UserSignUpForm()
    if request.method == 'POST':
        print("================")
        form=UserSignUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            password=form.cleaned_data['password1']
            email=form.cleaned_data['email']
            myform=form.save()
            print('form Saved')
            phone=request.POST['phone']
            # signals.profilesave.send(sender=None,instance=myform,phone=phone,created=True)
            signals.profilesave.send(sender=None,form=myform,phone=phone,created=True)
            print('profile saved')
            # print(email,password)
            user=authenticate(request,username=email,password=password)
            print(user)
            if user is not None:
                dj_login(request,user)
                return redirect('/')
        
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})