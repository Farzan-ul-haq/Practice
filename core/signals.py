from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import pre_init,pre_save,pre_delete,post_save,post_delete,post_init
from django.contrib.auth.models import User
from .models import *
from django.dispatch import receiver
from django.core.signals import request_finished,request_started,got_request_exception


#auth signals
@receiver(user_logged_in)
def login_success(sender,request,user, **kwargs):
    print('sender: ',sender)
    print('request: ',request)
    print('user email: ',user.email)
    print('user password: ',user.password)
    print('kwargs: ',kwargs)


@receiver(user_logged_out)
def logout_success(sender,request,user, **kwargs):
    print('sender: ',sender)
    print('request: ',request)
    print('user: ',user)
    print('**kwargs: ',kwargs)

@receiver(user_login_failed)
def login_failed(sender,credentials,request, **kwargs):
    print('sender: ',sender)
    print('credentials: ',credentials)
    print('request: ',request)
    print('**kwargs: ',kwargs)



# models signals

# @receiver(pre_save)
# def at_beginning_save(sender,instance,**kwargs):
#     print('Pre Save')
#     print('Sender:',sender)
#     print('instance:',instance)
#     print('kwargs:',kwargs)
# @receiver(post_save)
# def at_ending_save(sender,instance,created,**kwargs):
#     print('Post Save')
#     if created:
#         print('Sender:',sender)
#         print('instance:',instance)
#         print('created:',created)
#         print('kwargs:',kwargs)


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance,phone='0000000000000')
    
#request Symbols
@receiver(request_started)
def at_beginning_request(sender,environ,**kwargs):
    print('At beginning request')
    print('sender:',sender)
    print('environ:',environ)
    print('kwargs:',kwargs)

@receiver(request_finished)
def at_ending_request(sender,**kwargs):
    print('At ending request')
    print('sender:',sender)
    print('kwargs:',kwargs)

@receiver(got_request_exception)
def at_request_exception(sender,request,**kwargs):
    print('At beginning request')
    print('sender:',sender)
    print('request:',request)
    print('kwargs:',kwargs)

