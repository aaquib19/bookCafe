from django.db import models
from django.utils import timezone

class Feedback(models.Model):
    customer_name = models.CharField(max_length=120, null=False)
    email = models.EmailField(max_length=40, null=False)
    comments = models.TextField(null=False)
    book_name = models.CharField(max_length=120, null=False)

    date = models.DateField(auto_now=timezone.now)

    def __str__(self):
        return self.customer_name
