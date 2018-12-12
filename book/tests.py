from django.test import TestCase
from accounts.models import User
from book.models import *
from django.test.client import Client
from django.urls import reverse

class UsersListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(email='ronytowilson3097@gmail.com', password='devilmaycry4')

    def test_views_listview(self):
        response = self.client.get(reverse('book:list'))
        self.assertEquals(response.status_code, 200)


    # def test_views_detailview(self):
    # 	cls.book = Book.objects.create_book(title='title',slug='slug',isbn='isbn',pub_date='1999-12-12',authors='authors',publisher='publisher',no_of_actual_copy=45,no_of_copy_left=23,category='category',description='description')
    # 	response = self.client.get(reverse('book:detail/<slug>'))
    # 	self.assertEquals(response.status_code, 200) 


class AuthorModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Author.objects.create(name='hi',age=34)
	def test_name_label(self):
		author=Author.objects.get(id=1)
		field_label=author._meta.get_field('name').verbose_name
		self.assertEquals(field_label,'name')
	def test_age_label(self):
		author=Author.objects.get(id=1)
		field_label=author._meta.get_field('age').verbose_name
		self.assertEquals(field_label,'age')
	def test_name_max_length(self):
		author=Author.objects.get(id=1)
		max_length=author._meta.get_field('name').max_length
		self.assertEquals(max_length,100)


class PublisherModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Publisher.objects.create(name='hi')
	def test_name_label(self):
		publisher=Publisher.objects.get(id=1)
		field_label=publisher._meta.get_field('name').verbose_name
		self.assertEquals(field_label,'name')
	
	def test_name_max_length(self):
		publisher=Publisher.objects.get(id=1)
		max_length=publisher._meta.get_field('name').max_length
		self.assertEquals(max_length,200)
		
class CategoryModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Category.objects.create(name='hi')
	def test_name_label(self):
		category=Category.objects.get(id=1)
		field_label=category._meta.get_field('name').verbose_name
		self.assertEquals(field_label,'name')
	
	def test_name_max_length(self):
		category=Category.objects.get(id=1)
		max_length=category._meta.get_field('name').max_length
		self.assertEquals(max_length,150)
		
class BookModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Author.objects.create(name='hi',age=34)
		Publisher.objects.create(name='hi')
		Category.objects.create(name='hi')
		Book.objects.create(title='hi',isbn='is',pub_date='1999-12-12',authors=Author.objects.get(id=1),publisher=Publisher.objects.get(id=1),no_of_actual_copy=45,no_of_copy_left=23,category=Category.objects.get(id=1))
	def test_title_label(self):
		book=Book.objects.get(id=1)
		field_label=book._meta.get_field('title').verbose_name
		self.assertEquals(field_label,'name')
	def test_isbn_max_length(self):
		book=Book.objects.get(id=1)
		field_label=book._meta.get_field('isbn').max_length
		self.assertEquals(field_label,140)
	
	