from django.db import models
from django.db.models.query import QuerySet
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from borrower.models import token,pooled_token

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
        data = kwargs['instance']
        Notification.objects.create(
            recipient = data.user,
            notification_title = ("token number {}").format(data.token),
            description=("your token number for the book {} is {}. it will expire in 3 hours.please go and collect your book before token expire").format(data.book,data.token),
        )

# @receiver(post_save,sender = pooled_token)
# def sendnotification(sender,**kwargs):
#     if(kwargs['created']):
#         data = kwargs['instance']
#         print(data.user)
#         Notification.objects.create(
#             notification_title = ("token number {} for book pooled").format(data.token),
#             description=("your token number for the book {} is {}. it will expire in 3 hours.please go and collect your book before token expire").format(data.book,data.token),
#         )
