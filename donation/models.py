from django.db import models

# Create your models here.
class donation(models.Model):
	name = models.CharField(max_length=255,null=True,blank=True)
	emaild = models.EmailField(max_length=255)
	bookname=models.CharField(max_length=255,null=True,blank=True)