from borrower.models import token
from django.utils import timezone,duration
import datetime
from .models import Notification

def TokenExpire():
    '''for now it will work for every second'''
    qset = token.objects.filter(deleted=False)
    for tokens in qset:
        duration = timezone.now() - tokens.date
        if duration.total_seconds() > (3*60*60):
            print(tokens.user_name)
            Notification.objects.create(
                recipient = tokens.user_name,
                notification_title = "token no. "+str(tokens.token)+" expire :(",
                description="sorry! your token no."+str(tokens.token)+" for the book "+str(tokens.book_name)+" expire",
            )
            token.objects.filter(token = tokens.token).update(deleted=True)
