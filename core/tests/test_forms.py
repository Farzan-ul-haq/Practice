from django.test import SimpleTestCase,Client,TestCase
from core.forms import UserSignUpForm
from django import forms

class TestForms(TestCase):

    def setUp(self):
        self.client=Client()


    def test_user_signup_form(self):
        print('UserSignUpForm+++++++++++++++')
        form=UserSignUpForm(data={
            'email':'fake@email.com',
            'name':'Fake',
            'password1':'fkws1234',
            'password2':'fkws1234',
        })
        print(form.data['email'])
        self.assertEqual('fake@email.com',form.data['email'])
        self.assertTrue(form.is_valid())



