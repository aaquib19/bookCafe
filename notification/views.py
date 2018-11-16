from django.shortcuts import render
from django.views import generic
from .models import Notification

class NotificationList(generic.ListView):
    """here we have all the notifications for a specific user"""
    models = Notification
    template_name = 
