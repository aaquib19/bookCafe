from django.contrib import admin
from . models import Category,Publisher,Author,Book,Borrower_detail,Feedback,Request,token
# Register your models here.
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Borrower_detail)
admin.site.register(Feedback)
admin.site.register(Request)
admin.site.register(token)

