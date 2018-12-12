from django.contrib import admin

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'date', 'book_name', 'comments')
    list_filter = ('date', 'book_name',)
    search_fields = ('details', 'book_name',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
