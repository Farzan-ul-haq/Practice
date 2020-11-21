from django.test import TestCase,Client
from django.urls import reverse,resolve
from .. import views
from django.contrib.auth.models import User
from core.models import *
import json
from importlib import import_module
from .. import signals


class SimpleTest(TestCase):
    def create_session(self):
        from django.conf import settings
        engine=import_module(settings.SESSION_ENGINE)
        store=engine.SessionStore()
        store.save()
        return store

class TestViews(SimpleTest,TestCase):
    def setUp(self):
        self.create_session()
        self.client=Client()
        self.email='testuser1@gmail.com'
        self.password='12345'
        self.user=User.objects.create_superuser(email=self.email,password=self.password)
        self.phone='00000000000'
        

        # prof=Profile.objects.create(user=self.user,phone=phone)

    # def signal_setup(self,user,phone):

    # def handle_login(self,username,password):
    #     logged_in=self.client.login(username=username,password=password)

    # def handle_session(self,user_id):
    #     session=self.client.session
    #     session['_auth_user_id']=user_id
    #     session.save()

    def test_index_GET(self):
        print('======',self.user)
        self.create_session()
        signals.profilesave.send(sender=None,form=self.user,phone=self.phone,created=True)
        self.client.login(username=self.email,password=self.password)
        session=self.client.session
        session['_auth_user_id']=self.user.id
        session.save()


        # print(session)
        # # request.session={'hi':0}
        # # request.session['_auth_user_id']=self.user.id
        # for i,j in session.items():
        #     print(f'{i}\t{j}')
        # login=self.client.login(username='testuser@gmail.com',password='12345')
        response=self.client.get(reverse('index'))
        print(response)
        #self.assertEquals(response.status_code,200)
        #self.assertTemplateUsed(response,'login.html')