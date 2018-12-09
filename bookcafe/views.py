from django.shortcuts import render,redirect


def home(request):

    #print("book issed by user",request.user.book_issued.all())
    return render(request,"home.html")

def home1(request):

    #print("book issed by user",request.user.book_issued.all())
    return render(request,"category.html")

