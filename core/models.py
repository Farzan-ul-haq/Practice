from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from .managers import *

class User(AbstractBaseUser,PermissionsMixin):
    'Custom user model that support using emails instead of username'
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    objects=UserManager()
    USERNAME_FIELD= 'email'

    def __str__(self):
        return f"{self.id}:{self.name}"


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=15)
    image=models.ImageField(upload_to='profile-images',default='profile-images/default.png')

    def __str__(self):
        return self.user.name


class Category(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    author=models.ForeignKey(Profile,
                            on_delete=models.SET_NULL,
                            null=True,
                            related_name='profile')
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ForeignKey(Category,
                            null=True,
                            blank=True,
                            on_delete=models.CASCADE,
                            related_name='likes')
    timestamp=models.DateTimeField(auto_now_add=True)
    cover_image=models.ImageField(upload_to='post-images',null=True,blank=True)
    likes=models.ManyToManyField(Profile)
    objects   =PostManager()

    def __str__(self):
        return self.title + ' by '+ self.author.user.name


class Comment(models.Model):
    comment=models.TextField()
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.ForeignKey(Profile,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment[:7]}... by {self.author.user.name}"
