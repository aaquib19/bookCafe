from django.test import TestCase
from accounts.models import User
from django.test.client import Client
from django.urls import reverse

class notification_ViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(email='ronytowilson3097@gmail.com', password='devilmaycry4')

    def test_notification_alert(self):
        response = self.client.get(reverse('notification:notifications_list'))
        self.assertRedirects(response, '/login/?next=/notification/')

