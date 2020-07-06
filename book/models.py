import random
import os
from django.db.models.signals import pre_save

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.db.models import Q

from django.urls import reverse
from bookcafe.utils import unique_slug_generator

from bookcafe import settings

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    # print(filename)
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "media_/books/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    # slug

    def __str__(self):
        return str(self.name)


class Publisher(models.Model):
    name = models.CharField(max_length=200, unique=True)

    # slug

    def __str__(self):
        return str(self.name)


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()

    # slug

    def __repr__(self):
        return str(self.name)

    # def __str__(self):
    #     return str(self.name)

class BookQuerySet(models.query.QuerySet):

    def search(self,query):
        lookups =   ( Q(title__icontains=query) |
                      Q(isbn__icontains=query)

        )
        return self.filter(lookups).distinct()

class BookManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model,using=self._db)

    def search(self,query):
        return self.get_queryset().search(query)




class Book(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, unique=True)
    isbn = models.CharField(max_length=140, unique=True)
    pub_date = models.DateField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    no_of_actual_copy = models.IntegerField()
    no_of_copy_left = models.IntegerField()
    category = models.ManyToManyField(Category,related_name="books")
    image = models.ImageField(upload_to=upload_image_path)

    objects = BookManager()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        # similar to f"/book/{self.slug}/"
        return reverse("book:detail",kwargs={"slug":self.slug})

    #def get_issued_users(self):
        



    #def get_borrowed_users(self):


def book_pre_save_reciever(sender, instance, *args, **kwargs):
    #instance = kwargs["instance"]
    if instance.no_of_actual_copy < instance.no_of_copy_left:
        raise ValidationError("Number of actual copy is less than copy left")
    if instance.no_of_actual_copy < 0 or instance.no_of_copy_left < 0:
        raise ValidationError("check the number of copies")
    if not instance.slug:
        print("url ", instance.image.url)
        instance.slug = unique_slug_generator(instance)


pre_save.connect(book_pre_save_reciever, sender=Book)


class review(models.Model):
    rating=models.IntegerField()
    review=models.TextField(blank=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)

# class token(models.Model):
#     token=models.IntegerField()
#     user_name = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="un",on_delete=models.CASCADE,null=True)
#     #user_name = models.CharField(max_length=255,blank=True,null=True)
#     book_name = models.ForeignKey(Book,related_name="bn",on_delete=models.CASCADE,null=True,blank=True)
#     date = models.DateField(default=timezone.now)
#     class Meta:
#         unique_together=('user_name','book_name')



