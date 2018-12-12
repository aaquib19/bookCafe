# Create your tests here.
from django.test import Client, TestCase
from django.contrib.auth.models import User
from .models import Book
from django.urls import reverse


# TODO Set tests for logged in users, having different configurations like with and without more_user_data
# Check out the client login method https://docs.djangoproject.com/en/2.1/topics/testing/tools/#django.test.Client.login
# Check this request factory method out for above : https://docs.djangoproject.com/en/2.1/topics/testing/advanced/#example

# class SubmitSolutionUrlTest(TestCase):

#     def setUp(self):
#         # self.createduser = User.objects.create_user(username="testnormaluser", email="testnormaluser@ts.com",
#         #                                             password="Test Hello World")
#         self.book = Book.objects.create(title="SampleBook",slug="SampleBook",isbn="SampleIsbn",pub_date="2000-12-12",
#         	no_of_actual_copy=67,no_of_copy_left=35)
#         self.client = None
#         self.request_url = '/book/' + self.book.slug
#         # Create clients on the fly in the tests as login/logout is required

#     def test_anonymous_ping(self):
#         self.client = Client()
#         response = self.client.get(self.request_url)

#         self.assertRedirects(response, expected_url="/registration/login?next=" + self.request_url)

#     def test_authenticated_ping(self):
#         self.client = Client()
#         self.client.force_login(self.createduser)
#         response = self.client.get(self.request_url)
#         self.assertEqual(response.status_code, 200)

#     def test_authenticated_random_id_ping(self):
#         self.client = Client()
#         self.client.force_login(self.createduser)
#         response = self.client.get('/book/blahblah')
#         self.assertEqual(response.status_code, 404)
# class QuestionBrowseUrlTest(TestCase):

#     def setUp(self):
#         self.createduser = User.objects.create_user(username="testnormaluser", email="testnormaluser@ts.com",
#                                                     password="Test Hello World")
#         self.question = Question.objects.create(author=self.createduser, title="Sample Question",
#                                                 short_description="Sample Short Desc", description="Sample Descrption",
#                                                 unique_code="sq")
#         self.client = None
#         self.request_url = '/questions/browse'
#         # Create clients on the fly in the tests as login/logout is required

#     def test_anonymous_ping(self):
#         self.client = Client()
#         response = self.client.get(self.request_url)

#         self.assertEqual(response.status_code,200)


#     def test_authenticated_random_id_ping(self):
#         self.client = Client()
#         self.client.force_login(self.createduser)
#         response = self.client.get('/questions/blahblah/submit')
#         self.assertEqual(response.status_code, 404) 
             
# class QuestionPostUrlTest(TestCase):

#     def setUp(self):
#         self.createduser = User.objects.create_user(username="testnormaluser", email="testnormaluser@ts.com",
#                                                     password="Test Hello World")
#         self.question = Question.objects.create(author=self.createduser, title="Sample Question",
#                                                 short_description="Sample Short Desc", description="Sample Descrption",
#                                                 unique_code="sq")
#         self.client = None
#         self.request_url = '/questions/post/'
#         # Create clients on the fly in the tests as login/logout is required

#     def test_anonymous_ping(self):
#         self.client = Client()
#         response = self.client.get(self.request_url)

#         self.assertRedirects(response, expected_url="/registration/login?next=" + self.request_url)

    
#     def test_authenticated_ping(self):
#         self.client = Client()
#         self.client.force_login(self.createduser)
#         response = self.client.get(self.request_url)
#         self.assertEqual(response.status_code, 200)      


#     def test_authenticated_random_id_ping(self):
#         self.client = Client()
#         self.client.force_login(self.createduser)
#         response = self.client.get('/questions/blahblah/post/')
#         self.assertEqual(response.status_code, 404)



# from django.contrib.auth.models import User
# Create your tests here.


class TestUser(TestCase):
 
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
