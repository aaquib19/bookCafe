from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
import json

# Create your views here.
from django.http import HttpResponse
from django.views import View
from .models import Tag
from .forms import  SearchTagForm


class SearchTag(View):
    """ Search tags with autocomplete (live search) """

    def get(self, request):
        form = SearchTagForm()
        context = {'searchtag' : form}
        return render(request, 'tag/search_tags.html', context)

    def post(self,request):
        q = request.POST['q']
        print("qery =",q)
        form = SearchTagForm()
        tags = Tag.objects.filter(title__icontains=q)
        context = {'tags' : tags, 'searchtag' : form}
        return render(request, 'tag/search_tags.html', context)

class TagJson(View):
    """ Search tags with autocomplete (live search) json data"""
    def get(self, request):
        q = request.GET.get('q', '')
        print(q)
        taglist = []
        tags = Tag.objects.filter(title__icontains=q) #this function shows the popup data
        for tag in tags:
            new = {'q' : tag.title, 'count' : 1}
            taglist.append(new)
        return HttpResponse(json.dumps(taglist), content_type="application/json")


















