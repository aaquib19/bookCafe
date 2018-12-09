from django.contrib import admin
from django.urls import include,path

from . import views

urlpatterns = [
    path("",views.donate,name="donate"),
    path("adduser",views.adduser,name="adduser"),
    

]