from django.db import models
from django.db.models.query import QuerySet
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from borrower.models import token,pooled_token
from events.models import borrower_detail

class NotificationQuerySet(models.query.QuerySet):
    ''' Notification QuerySet '''
    def unsent(self):
        return self.filter(emailed=False)

    def sent(self):
        return self.filter(emailed=True)

    def unread(self, include_deleted=False):
        """Return only unread items in the current queryset"""
        return self.filter(unread=True)

    def read(self, include_deleted=False):
        """Return only read items in the current queryset"""
        return self.filter(unread=False)

    def mark_all_as_read(self, recipient=None):
        """Mark as read any unread messages in the current queryset.
        Optionally, filter these by recipient first.
        """
        qset = self.unread(True)
        if recipient:
            qset = qset.filter(recipient=recipient)
        return qset.update(unread=False)

    def mark_all_as_unread(self, recipient=None):
        qset = self.read(True)
        if recipient:
            qset = qset.filter(recipient=recipient)
        return qset.update(unread = True)

    def mark_as_unsent(self, recipient=None):
        qset = self.sent()
        if recipient:
            qset = qset.filter(recipient=recipient)
        return qset.update(emailed=False)

    def mark_as_sent(self, recipient=None):
        qset = self.unsent()
        if recipient:
            qset = qset.filter(recipient=recipient)
        return qset.update(emailed=True)

class Notification(models.Model):
    #user to whom notification to be sent
    recipient = models.ForeignKey(User,default='',related_name='notifications',on_delete=models.CASCADE)
    unread = models.BooleanField(default=True, blank=False, db_index=True)
    notification_title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    emailed = models.BooleanField(default=False, db_index=True)
    description_view = models.BooleanField(default=False,db_index=True)
    objects = NotificationQuerySet.as_manager()


@receiver(post_save,sender = User)
def welcome_msg(sender,**kwargs):
    if kwargs['created']:
        Notification.objects.create(
            recipient = kwargs['instance'],
            notification_title = "Welcome to BOOKCAFE!!",
            description="thanks for signing up :)",
        )

@receiver(post_save,sender = token)
def sendnotification(sender,**kwargs):
    if(kwargs['created']):
        tokens = kwargs['instance']
        query = list()
        if tokens.user is not None:
            query.append(tokens.user)
        if tokens.user2 is not None:
            query.append(tokens.user2)
        if tokens.user3 is not None:
            query.append(tokens.user3)
        title = "token no. "+str(tokens.token)
        if len(query) > 1:
            title = ("token no. {} for pooled book").format(tokens.token)
        for user in query:
            Notification.objects.create(
                recipient = user,
                notification_title = title,
                description="your token no. "+str(tokens.token)+" for the book "+str(tokens.book)+".it will expire in 3 hours please go and collect before that",
            )

@receiver(post_save,sender = borrower_detail)
def welcome_msg(sender,**kwargs):
    if kwargs['created']:
        data = kwargs['instance']
        query = data.pooled_users.all()
        Notification.objects.create(
            recipient = data.name,
            notification_title = ("your book {} is issued").format(data.book_name),
            description="we have succesfully received your book issue comfirmation",
        )
        for user in query:
            Notification.objects.create(
                recipient = user,
                notification_title = ("your book {} is issued").format(data.book_name),
                description="we have succesfully received your book issue comfirmation",
            )
