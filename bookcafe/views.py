from django.shortcuts import render, redirect, render_to_response


def home(request):

    #print("book issed by user",request.user.book_issued.all())
    return render(request,"home.html")
