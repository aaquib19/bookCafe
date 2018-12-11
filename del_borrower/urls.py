from django.contrib import admin
from django.urls import include,path

from . import views

urlpatterns = [
    path("",views.disp_borrowers,name="disp_borrowers"),
    # path("adduser",views.adduser,name="adduser"),
    path("del", views.del_borrower, name="del"),

]