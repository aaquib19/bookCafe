
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.BookListView.as_view(),name="list"),
    path("<slug:slug>/", views.BookDetailView.as_view(), name="detail"),

    #demo how to use string
    #path("test/<str:url_string>/", views.test, name="test"),

    path("check_book/<slug:url_string>/", views.check_book, name="check_book"),
    path("token/<slug:booktoken>/", views.gen_token, name="token"),

	path("undo/<slug:booki>/", views.undo, name="undo"),


]