from django.conf.urls import url

from . import views

app_name = 'form'
urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'', views.feedback_form, name='feedback-page'),
    url(r'^logout/$', views.user_logout, name='logout'),
]
