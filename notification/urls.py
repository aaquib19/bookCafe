from django.urls import path
from .views import NotificationList,mark_all_read,mark_all_unread,delete_all_notification

app_name ='notification'
urlpatterns = [
    path('',NotificationList.as_view(),name = 'notifications_list'),
    path('markallasread/',mark_all_read,name="markallasread"),
    path('markallasunread/',mark_all_unread,name="markallasunread"),
    path('deletenotification/',delete_all_notification,name="deletenotification"),
]
