from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns=[
    path('',views.index,name='index'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'),name='ins.login'),
    path('register/',views.register,name='register'),
]
