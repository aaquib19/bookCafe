from django.urls import path
from . import views



app_name = 'cat1books'

urlpatterns = [
    path('', views.home,name='c1home'),
    path('desc',views.desc,name='desc'),
	path('checkBook/', views.check_book,name='confirm.book'),
	path('token/', views.generate_token,name='token'),
]
