# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.db.models.signals import m2m_changed
from bookcafe import settings
from book.models import Book
# Create your models here.


class borrower_detail(models.Model):
    borrowed_id         = models.CharField(max_length=123,null=True,blank=True)
    name                = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    book_name           = models.ForeignKey(Book,on_delete=models.CASCADE,null=True,blank=True)
    issue_date          = models.DateField()
    returning_date      = models.DateField(null=True,blank=True)
    submission_date     = models.DateField()
    pooled_users        = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='book_pooling_users')
    deleted             = models.BooleanField(default=False)
    #title               = models.BooleanField(default=True)

    #slug
    class Meta:
        unique_together = ('name','book_name')

    def __str__(self):
        return str(self.name)

    # def clean(self,*agrs,**kwargs):
    #     if self.book_name.count() > 2:
    #         print("count = ",self.book_name.count())
    #         raise ValidationError("you cannot issue for more than 2 books")
    #     super(Borrower_detail,self).clean(*agrs,**kwargs)
    # class Meta:
    #     verbose_name = u'Scheduling'
    #     verbose_name_plural = u'Scheduling'

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.name))



# def book_issued(sender,**kwargs):
#     if kwargs["instance"].book_name.count()>2:
#         print("count = ",kwargs["instance"].book_name.count())
#         raise ValidationError("you cannot issue more than 2 book")

# m2m_changed.connect(book_issued,sender=borrower_detail.book_name.through)

#

# def pooled_users_check(sender,**kwargs):
#     instance = kwargs["instance"]
#     print("people  ",instance.pooled_users)
#     if instance.pooled_users.count() > 2:
#         print("hello")
#         raise ValidationError("only 3 people can pool a single book")
#     if instance.name in instance.pooled_users.all():
#         raise ValidationError("user is in pooled list")

#m2m_changed.connect(pooled_users_check,sender=borrower_detail.pooled_users.through)
# m2m_changed.connect(pooled_users_check,sender=borrower_detail.pooled_users.through)

