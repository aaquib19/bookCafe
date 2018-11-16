
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.category,name="category"),
    
    # path("category/<str:subject>", views.category, name="category"),  # this is temprory subjects/science

]