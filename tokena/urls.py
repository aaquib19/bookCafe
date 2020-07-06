from django.contrib import admin
from django.urls import include,path

from . import views

urlpatterns = [
    path("",views.disp_tokens,name="disp_tokens"),
    # path("adduser",views.adduser,name="adduser"),
    path("<int:tokenNo>/", views.add_book, name="add_book"),

]