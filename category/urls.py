
from django.urls import path,include
from . import views

urlpatterns = [

    path('<str:category>',views.CategoryListView.as_view(),name="home"),
    
    # path("category/<str:subject>", views.category, name="category"),  # this is temprory subjects/science

]