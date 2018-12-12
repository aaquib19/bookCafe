from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
#
# def category(request):
#     return  render(request,"category/category_home.html")

from book.models import Book
from book.models import Category

class CategoryListView(ListView):
    template_name = "category/category_home.html"
    paginate_by = 9
    #queryset = Book.objects.all()

    def get_queryset(self,*args,**kwargs):
        #category = self.request.GET.get('category')

        category = self.kwargs['category']
        if category == "all":
            return Book.objects.all()

        a = Category.objects.get(name=category)
        return a.books.all()
