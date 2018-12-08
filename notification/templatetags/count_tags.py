from django import template
from notification.models import Notification


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
