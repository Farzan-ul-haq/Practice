from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import *
urlpatterns=[
    path('',views.index,name='index'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html',
                                                authentication_form=UserLoginForm),
        name='ins.login'),
    path('register/',views.register,name='register'),
]
