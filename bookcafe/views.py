from django.shortcuts import render,redirect


def home(request):
    return render(request,"home.html",{})

def index(request):
    return render(request,"home_.html",{})