from django.contrib import admin
from django.urls import path

from .views import emailView,successView

urlpatterns = [
	path('',emailView,name = 'submit'),
	path('success/',successView,name = 'success')
]