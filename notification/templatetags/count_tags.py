from django import template
from notification.models import Notification
from events.models import borrower_detail as bd
from del_borrower.views import cal_fine
from datetime import datetime,timedelta
register = template.Library()
@register.simple_tag(takes_context = True)
def readtag(context):
    user = context['request'].user
    return Notification.objects.filter(recipient = user).filter(unread = False).count()

@register.simple_tag(takes_context = True)
def unreadtag(context):
    user = context['request'].user
    return Notification.objects.filter(recipient = user).filter(unread = True).count()

@register.simple_tag(takes_context = True)
def emailedtag(context):
    user = context['request'].user
    return Notification.objects.filter(recipient = user).filter(emailed = True).count()

@register.simple_tag(takes_context = True)
def finecal(context,id):
    p = bd.objects.get(pk=id)
    return cal_fine(datetime.now().date(),p.submission_date)
