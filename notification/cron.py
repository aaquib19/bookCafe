from borrower.models import token
from django.utils import timezone,duration
import datetime
from .models import Notification

def TokenExpire():
    '''for now it will work for every second'''
    qset = token.objects.filter(deleted=False)
    for tokens in qset:
        duration = timezone.now() - tokens.date
        print(duration.total_seconds())
        if duration.total_seconds() > 1:
            print(tokens.user)
            Notification.objects.create(
                recipient = tokens.user,
                notification_title = "token no. "+str(tokens.token)+" expire :(",
                description="sorry! your token no. "+str(tokens.token)+" for the book "+str(tokens.book)+" expire",
            )
            token.objects.filter(token = tokens.token).update(deleted=True)
