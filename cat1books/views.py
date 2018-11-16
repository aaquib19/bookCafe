from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from . models import Book,Borrower_detail,token,Request
from django.contrib.auth.models import User

def home(request):
	context={
		'Books':Book.objects.all()
	}
	return render(request,'cat1books/home.html',context)

def desc(request):
	book=Book.objects.all().first()#objects.all().first()(id=1)
	#b=[book.name,book.authors]
	book_name=book.name
	authors=book.authors
	publisher=book.publisher
	#values =[book_name,authors,publisher]
	
	user = request.user
	values=[user,book]
	#return HttpResponse("<h1> {{ book.name }} </h1>")
	return render(request,'cat1books/des.html',{'values':values})



def check_book(request):

	#form = login_form()print(request.user)
	placeholder = ""
	user = request.user
	#print(typeof(user))
	#print(user.is_authenticated())
	values=[]
	#if request.method == 'POST':
	#	username = request.POST['username']
	book=Book.objects.all().first()#objects.all().first()(id=1)
	print(book.name)
	book_name=book.name
	authors=book.authors
	publisher=book.publisher
	#values =[book_name,authors,publisher]
	values=book
	print(book_name,authors,publisher)


	if not request.user.is_authenticated:
		messages.error(request,"You need to login inorder to issue a book")
		#return render(request,'bookissue/issue.html')
		return redirect('desc')
		
	else:
		if book.no_of_copy_left==0:
			messages.error(request,"There is no stock available!")
			return redirect('desc')
		else:
			return render(request, 'cat1books/bookform2.html',{'user':user,'values':values})



import random
import time
def generate_token(request):
	t0=time.time()
	tokens=random.randint(1, 3910209312)
	messages.success(request,"Your token is {}".format(tokens))
	book=Book.objects.all().first()
	#book=book.objects.filter(name=book)
	#Token=token()
	#user=Request.user_name
	user1 = request.user
	user=User.objects.filter(username=user1)
	#Token.user_name=user
	#Token.token=tokens
	token.objects.create(token=tokens,user_name_id=user1.id,book_name_id=book_id)
	#token.save(self)
	
	book.no_of_copy_left=book.no_of_copy_left-1
	book.save()
	
	return redirect('desc')


#def confirm_book(request):

#	Book.no_of_copy_left-1

	#if request.method =='POST'

	#	username=request.POST['username']
	#	book_name=request.POST['bookname']
	#	issue_date=request.POST['issuedate']
	#	returning_date=request.POST['returndate']
	#	Borrower_detail.Createobjects()
	#return render(request,)

