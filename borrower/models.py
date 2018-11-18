from django.db import models

# Create your models here.
from book.models import Book
#from django.contrib.auth.models import User
from bookcafe import settings
from django.utils import timezone

class token(models.Model):
    token=models.IntegerField()
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="un",on_delete=models.CASCADE,null=True,blank=True)
    #user_name = models.CharField(max_length=255,blank=True,null=True)
    book_name = models.ForeignKey(Book,related_name="bn",on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(default=timezone.now)
    class Meta:
        unique_together=('user_name','book_name')


class pooled_token(models.Model):
	token = models.IntegerField()
	main_user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="pooled_un",on_delete=models.CASCADE)
	pooled_user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="pooled_user")
	book_name = models.ForeignKey(Book,related_name="pooled_bn",on_delete=models.CASCADE,null=True,blank=True)
	date = models.DateField(default=timezone.now)

	# class Meta:
	# 	unique_together=('main_user','book_name')