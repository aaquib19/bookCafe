from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='c1home'),
    path('desc',views.desc,name='desc'),
	path('checkBook/', views.check_book,name='confirm.book'),
	path('token/', views.generate_token,name='token'),
]
