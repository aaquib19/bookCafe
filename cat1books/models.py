from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models.signals import m2m_changed
from django.contrib.auth.models import User

from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager
)

from bookcafe import settings
# Create your models here.


class Category(models.Model):
    name    = models.CharField(max_length=150,unique=True)
    #slug


    def __str__(self):
        return str(self.name)

class Publisher(models.Model):
    name    = models.CharField(max_length=200,unique=True)
    #slug

    def __str__(self):
        return str(self.name)


class Author(models.Model):
    name     = models.CharField(max_length=100,unique=True)
    age      = models.IntegerField()

    #slug
    
    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    name                = models.CharField(max_length=150)
    isbn                = models.CharField(max_length=140,unique=True)
    pub_date            = models.DateField()
    authors             = models.ManyToManyField(Author)
    publisher           = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    no_of_actual_copy   = models.IntegerField()
    no_of_copy_left     = models.IntegerField()
    category            = models.ManyToManyField(Category)
    image               = models.ImageField()
    #slug
    
    def __str__(self):
        return str(self.name)


class Borrower_detail(models.Model):
    name                = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    book_name           = models.ManyToManyField(Book)
    issue_date          = models.DateField()
    returning_date      = models.DateField()
    submission_date     = models.DateField()
    pooled_users        = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='book_pooling_users')
    #slug

    def __str__(self):
        return str(self.name)

    # def clean(self,*agrs,**kwargs):
    #     if self.book_name.count() > 2:
    #         print("count = ",self.book_name.count())
    #         raise ValidationError("you cannot issue for more than 2 books")
    #     super(Borrower_detail,self).clean(*agrs,**kwargs)

def book_issued(sender,**kwargs):
    if kwargs["instance"].book_name.count()>2:
        print("count = ",kwargs["instance"].book_name.count())
        raise ValidationError("you cannot issue more than 2 book")

m2m_changed.connect(book_issued,sender=Borrower_detail.book_name.through)

def pooled_users_check(sender,**kwargs):
    instance = kwargs["instance"]
    print("people  ",instance.pooled_users)
    if instance.pooled_users.count() > 2:
        print("hello")
        raise ValidationError("only 3 people can pool a single book")
    if instance.name in instance.pooled_users.all():
        raise ValidationError("user is in pooled list")

m2m_changed.connect(pooled_users_check,sender=Borrower_detail.pooled_users.through)

class Feedback(models.Model):
    book_name = models.ForeignKey(Book,on_delete=models.CASCADE,null=True,blank=True)
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    content   = models.TextField()


    def __str__(self):
        return str(self.book_name) + "--"+ str(self.user_name)

class Request(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    book_name = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_name)


class token(models.Model):
    token=models.IntegerField()
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    book_name = models.ForeignKey(Book,on_delete=models.CASCADE)
    
    class Meta:
        unique_together=('user_name','book_name')