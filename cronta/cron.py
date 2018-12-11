import sys, os
from datetime import datetime
from django.core.mail import send_mass_mail, mail_admins
from cronta.models import EmailQueue
from django.utils import timezone
from datetime import datetime,timedelta

def send_emails():
    """
    Send mass e-mails. Mark them and update the sent date.
    If an error is encountered notify admins
    """
    try:
        mass = []
        sent_queues = []
        email_queues = EmailQueue.objects.exclude(sent=True).all()
        for queue in email_queues:
            if queue.scheduled_datetime >= timezone.now().date():
                sent_queues.append(queue.pk)
                mass.append((queue.mail_subject, queue.mail_body,queue.mail_from, [queue.mail_to], ))
        send_mass_mail(tuple(mass))
        EmailQueue.objects.filter(pk__in=sent_queues).update(sent=True,sent_datetime=datetime.now())
    except Exception as e:
        mail_admins("django_emailqueue exception", str(e))

def my_jobs():
    send_emails()
