from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.views.generic import ListView,DetailView

from .models import Book
# Create your views here.

class BookListView(ListView):
    template_name = "book/list.html"
    queryset = Book.objects.all()


class BookDetailView(DetailView):
    template_name = "book/detail.html"
    queryset = Book.objects.all()

    def get_object(self, *args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Book.objects.get(slug=slug)
        except Book.DoesNotExist:
            raise Http404("book not found")
        except Book.MultipleObjectsReturned:
            qs = Book.objects.filter(slug=slug)
            instance= qs.first()
        except:
            raise Http404("some error has occured check detail view")
        return  instance
