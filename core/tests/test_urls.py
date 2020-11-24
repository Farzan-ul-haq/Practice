from django.test import TestCase,SimpleTestCase
from .. import views
from django.urls import resolve,reverse

class TestUrls(SimpleTestCase):
    def test_index_urls_is_resolved(self):
        print('WORKING')
        url = reverse('index')
        self.assertEquals(resolve(url).func,views.index )

    def test_register_urls_is_resolved(self):
        print('WORKING')
        url = reverse('register')
        self.assertEquals(resolve(url).func,views.register )
        