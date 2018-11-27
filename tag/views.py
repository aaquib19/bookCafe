from django.shortcuts import render
import json

# Create your views here.
from django.http import HttpResponse
from django.views import View
from .models import Tag
from book.models import Book

class SearchTag(View):
    """ Search tags with autocomplete (live search) """

    def get(self, request):
        context = {}#'form' : form}
        return render(request, 'tag/search_tags.html', context)

    def post(self,request):
        q = request.POST['q']
        print("qery =",q)
        tags = Book.objects.filter(title__icontains=q)
        print(tags)
        context = {'tags' : tags}#, 'form' : form}
        return render(request, 'tag/search_tags.html', context)

class TagJson(View):
    """ Search tags with autocomplete (live search) json data"""
    def get(self, request):
        q = request.GET.get('q', '')
        print(q)
        taglist = []
        #tags = Tag.objects.filter(title__icontains=q) #this function shows the popup data
        tags = Book.objects.filter(title__icontains=q)

        for tag in tags:
            new = {'q' : tag.title}
            taglist.append(new)
        return HttpResponse(json.dumps(taglist), content_type="application/json")


















