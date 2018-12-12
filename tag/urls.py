from django.urls import path,include

from . import views

urlpatterns = [
    path('hashtag/', views.SearchTag.as_view(),name="ajax_search"),
    path('hashtag.json', views.TagJson.as_view()),
]

