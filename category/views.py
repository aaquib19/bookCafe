from django.shortcuts import render

# Create your views here.

def category(request):
    return  render(request,"category/category_home.html")
