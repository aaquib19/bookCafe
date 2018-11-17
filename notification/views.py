from django.shortcuts import render
from django.views import generic
from .models import Notification
from accounts.models import User
from django.shortcuts import get_object_or_404

class NotificationList(generic.ListView):
    """here we have all the notifications for a specific user"""
    template_name = 'notification/home.html'
    context_object_name = 'notifications'
    def get_queryset(self):
        return Notification.objects.filter(recipient = self.request.user).order_by('timestamp')

class NotificationDetail(generic.DeleteView):
    template_name = 'notification/detail.html'
    context_object_name = 'notice'
    def get_queryset(self):
        _id = self.kwargs.get("pk")
        return Notification.objects.filter(id=_id)
