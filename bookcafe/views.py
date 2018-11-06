from django.shortcuts import render,redirect


def home(request):
    return render(request,"home.html")

def category(request):
    return  render(request,"category.html")

