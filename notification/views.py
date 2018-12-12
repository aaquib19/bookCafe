from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Notification
from accounts.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notification

class NotificationList(LoginRequiredMixin,generic.ListView):
    """here we have all the notifications for a specific user"""
    template_name = 'notification/home.html'
    context_object_name = 'notifications'
    def get_queryset(self):
        #Notification.objects.mark_all_as_read(recipient = self.request.user)
        return Notification.objects.filter(recipient = self.request.user).order_by('timestamp').reverse()

def mark_all_read(request):
    user = request.user
    Notification.objects.mark_all_as_read(recipient = user)
    return HttpResponseRedirect(reverse('notification:notifications_list'))

def mark_all_unread(request):
    user = request.user
    Notification.objects.mark_all_as_unread(recipient = user)
    return HttpResponseRedirect(reverse('notification:notifications_list'))

def delete_all_notification(request):
    user = request.user
    qset = Notification.objects.filter(recipient = user)
    for notice in qset:
        qset.delete()
    return HttpResponseRedirect(reverse('notification:notifications_list'))
