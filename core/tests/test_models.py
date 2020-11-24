from django.test import TestCase
from core.models import *
from .. import signals

class TestModel(TestCase):

    def setUp(self):
        self.superuser=User.objects.create_superuser('Fake SuperUser','fkpass')
        self.user=User.objects.create_user('FakeEmail','fkpass',name='Fakename')
        signals.profilesave.send(sender=None,form=self.user,phone='012513214',created=True)
        self.profile=Profile.objects.get(user=self.user)
        self.categ=Category.objects.create(title='FAKe Category')
        self.post=Post.objects.create_post(self.profile,'Fake Post','Fake Content',self.categ,' ')
        
    def test_model_post_create_post(self):
        self.author=self.profile
        self.title='Fake TEsting Title'
        self.content='Fake TEsting Title'
        self.category=self.categ
        self.post=Post.objects.create_post(self.author,self.title,self.content,self.category,'')
        self.assertEqual(self.title,self.post.title)

    def test_model_post_collect_post(self):
        self.post1=Post.objects.get_post(self.profile)
