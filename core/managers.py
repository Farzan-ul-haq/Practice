from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        "create a new user"
        if not email:
            raise ValueError('User must hava an email address')
        user=self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,**kwargs):
        'Create a new super user'
        user=self.create_user(email,password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class PostManager(models.Manager):
    def create_post(self,title,content,category,cover_image):
        print(self)

        post=self(author=Profile.objects.first(),
                title=title,
                content=content,
                category=category,
                cover_image=cover_image
                ).save()
        return post
