from django.test import TestCase

from accounts.models import User
from django.test.client import Client
from django.urls import reverse

class UsersListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(email='ronytowilson3097@gmail.com', password='devilmaycry4')

    def test_search(self):
        response = self.client.get(reverse('search:query'))
        self.assertEquals(response.status_code, 200

)