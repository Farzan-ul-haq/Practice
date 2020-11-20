from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import *
urlpatterns=[
    #Index
    path('',views.index,name='index'),
    #Auth View Login logout
    path('login/', auth_view.LoginView.as_view(template_name='login.html',
                                                authentication_form=UserLoginForm),
        name='login'),
    path('logout/',views.handlelogout,name='logout'),
    path('register/',views.register,name='register'),
]
