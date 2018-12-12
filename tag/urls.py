from django.urls import path,include

from . import views

urlpatterns = [
    path('hashtag/', views.SearchTag.as_view()),
    path('hashtag.json', views.TagJson.as_view()),
]

