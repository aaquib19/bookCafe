from django.shortcuts import render,redirect


def home(request):

    #print("book issed by user",request.user.book_issued.all())
    return render(request,"home.html")

def category(request):
    return  render(request,"category.html")

