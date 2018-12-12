from django.test import TestCase

from .models import User
from django.test.client import Client
from django.urls import reverse


# from django.contrib.auth.models import User
# Create your tests here.


class TestUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(first_name='wilson', last_name='patro',
                                   email='ronytowilson3097@gmail.com', password='12345wilson')

    def test_user(self):
        user = User.objects.get(id=1)

        exepected_value = f'{user.first_name}, {user.last_name}, {user.email}'
        self.assertEquals(user.testinguser(), str(exepected_value))

    def test_maxlength(self):
        user = User.objects.get(id=1)
        maximamlength=user._meta.get_field('first_name').max_length
        self.assertEquals(maximamlength,255)

#Now for testing views


class UsersListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(email='ronytowilson3097@gmail.com', password='devilmaycry4')


    def test_view_uses_correct_template_index(self):
            response = self.client.get(reverse('accounts:student_signup_new'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'accounts/student_signup.html')

    def test_view_url_accessible_by_name_profile(self):
        self.client.login(email='ronytowilson3097@gmail.com', password='devilmaycry4')
        response = self.client.get(reverse('accounts:view_profile'))
        self.assertTemplateUsed(response, 'accounts/profile.html')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name_logout(self):
        self.client.login(email='ronytowilson3097@gmail.com', password='devilmaycry4')
        response = self.client.get(reverse('logout'))
        # self.assertTemplateUsed(response, 'home/index.html')
        self.assertRedirects(response, '/')
