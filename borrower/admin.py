from django.contrib import admin
from .models import token,pooled_token
# Register your models here.
admin.site.register(token)
admin.site.register(pooled_token)