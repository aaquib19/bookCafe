from borrower.models import token
from django.utils import timezone,duration
import datetime
from notification.models import Notification
from book.models import Book
from events.models import borrower_detail

def TokenExpire():
    '''for now it will work for every second'''
    qset = token.objects.filter(deleted=False)
    for tokens in qset:
        duration = timezone.now() - tokens.date
        if duration.total_seconds() > (2*60):
            query = list()
            if tokens.user is not None:
                query.append(tokens.user)
            if tokens.user2 is not None:
                query.append(tokens.user2)
            if tokens.user3 is not None:
                query.append(tokens.user3)
            title = "token no. "+str(tokens.token)+" expire :("
            if len(query) > 1:
                title = ("token no. {} for pooled book expire :(").format(tokens.token)
            for user in query:
                Notification.objects.create(
                    recipient = user,
                    notification_title = title,
                    description="sorry! your token no. "+str(tokens.token)+" for the book "+str(tokens.book)+" expire",
                )
            copies = Book.objects.get(title = tokens.book).no_of_copy_left
            Book.objects.filter(title = tokens.book).update(no_of_copy_left = copies+1)
            token.objects.filter(token = tokens.token).delete()


    qset = borrower_detail.objects.all()
    for detail in qset:
        if detail.returning_date == timezone.now().date()+datetime.timedelta(days = 1):
            users = detail.pooled_users.all()
            Notification.objects.create(
                recipient = detail.name,
                notification_title = ("due date tommorow book {}").format(detail.book_name),
                description=("your due date of submission for book {} is tommorow.please go and submit your book otherwise after that you have to pay fine").format(detail.book_name),
            )
            for user in users:
                Notification.objects.create(
                    recipient = user,
                    notification_title = ("due date tommorow book {}").format(detail.book_name),
                    description=("your due date of submission for book {} is tommorow.please go and submit your book otherwise after that you have to pay fine").format(detail.book_name),
                )
