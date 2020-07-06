

# Create your tests here.
from django.test import TestCase
from accounts.models import User
from django.test.client import Client
from django.urls import reverse

class donar_ViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(email='ronytowilson3097@gmail.com', password='devilmaycry4')

    def test_donar_as_user(self):

        response = self.client.get(reverse('donation:donate'))
        self.assertEquals(response.status_code, 200)

    def test_donar_Add_user(self):
        response = self.client.get(reverse('donation:donate'))
        self.assertEquals(response.status_code, 200)


