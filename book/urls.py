
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.BookListView.as_view(),name="list"),
    path("<slug:slug>/", views.BookDetailView.as_view(), name="detail"),


    #demo how to use string
    #path("test/<str:url_string>/", views.test, name="test"),

    path("check_book/<slug:url_string>/", views.check_book, name="check_book"),
    path("check_bookp/<slug:url_string>/", views.check_bookp, name="check_bookp"),
    path("gen_token/<slug:booktoken>/", views.gen_token, name="gen_token"),
    path("gen_tokenp/<slug:booktoken>/", views.gen_tokenp, name="gen_tokenp"),
	path("undo/<slug:booki>/", views.undo, name="undo"),
	path("reviews/<slug:bookn>/", views.reviews, name="reviews"),


]
