from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from book.models import Book
from django.http import HttpResponse
from .models import *


def home(request):
    return render(request, 'home.html')


def feedback_form(request):
    id = request.POST.get("book_id")
    book = Book.objects.get(id=id)
    print(book.title)
    if request.user.is_authenticated:
        obj = Book.objects.all()
        user = request.user.username
        email = request.user.email
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('form:home')
        else:
            form = FeedbackForm()
        return render(request, 'feedback_form.html', {'form': form, 'user': user, 'email': email ,"object" :book })
    else:
        return redirect('login')

@login_required
def user_logout(request):
    logout(request)
    return redirect('form:home')
