from django.urls import path
from .views import NotificationList,NotificationDetail

app_name ='notification'
urlpatterns = [
    path('',NotificationList.as_view(),name = 'notifications_list'),
    path('<int:pk>/',NotificationDetail.as_view(),name='notification_details')
]
