from django.db import models

from book.models import Book
from bookcafe import settings
from django.utils import timezone


class token(models.Model):
    token=models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="user",on_delete=models.CASCADE,null=True,blank=True)
    book = models.ForeignKey(Book,related_name="book",on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)

    class Meta:
        unique_together=('user','book')


class pooled_token(models.Model):
    token=models.IntegerField()
    main_user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="pooled_token",on_delete=models.CASCADE)
    pooled_user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="pooled_user")
    book = models.ForeignKey(Book,related_name="pooled_bn",on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(default=timezone.now)

    # class Meta:
    # 	unique_together=('main_user','book_name')
