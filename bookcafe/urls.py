"""bookcafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

from .import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from . import views
#from accounts.views import  LoginView,RegisterView


urlpatterns = [
    path("",views.home,name="home"),
    path("home",views.home1,name="home1"),
    #path('login/', LoginView.as_view(), name='login'),
    #path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),#accounts:logout

    # path("category/", views.category, name="category"),
    # path("category/<str:subject>", views.category, name="category"),  # this is temprory subjects/science

    path('admin/', admin.site.urls),
    path('book/', include(('book.urls', 'book'), namespace='book')),
    path('category/', include(('category.urls', 'category'), namespace='category')),

    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('search/', include(('search.urls', 'search'), namespace='search')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
