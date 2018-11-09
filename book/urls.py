
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.BookListView.as_view(),name="list"),
    path("<slug:slug>/", views.BookDetailView.as_view(), name="detail"),

]