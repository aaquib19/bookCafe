from django.contrib import admin
from .models import Notification
# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'notification_title', 'unread','description_view', 'emailed', )
    date_hierarchy = 'timestamp'
    list_filter = ('description_view', )

admin.site.register(Notification,NotificationAdmin)
