from django.contrib import admin

# Register your models here.
from .models import token

class TokenAdmin(admin.ModelAdmin):
    list_display = ('token','user_name','book_name','deleted')
    date_hierarchy = 'date'


admin.site.register(token,TokenAdmin)
