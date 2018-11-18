from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.views.generic import ListView,DetailView
from django.contrib import messages
from .models import Book
from tok.models import token
from django.utils import timezone
# Create your views here.

class BookListView(ListView):
    template_name = "book/list.html"
    queryset = Book.objects.all()


class BookDetailView(DetailView):
    template_name = "book/detail.html"
    queryset = Book.objects.all()

    def get_object(self, *args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Book.objects.get(slug=slug)
        except Book.DoesNotExist:
            raise Http404("book not found")
        except Book.MultipleObjectsReturned:
            qs = Book.objects.filter(slug=slug)
            instance= qs.first()
        except:
            raise Http404("some error has occured check detail view")
        return  instance


    def get_context_data(self,**kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            user = self.request.user
            context['user'] = user
            context['token'] = token.objects.filter(user_name=user)
        # Add in a QuerySet of all the books
        
        print(token.book_name)
        return context


def test(request, url_string):
    print(url_string)
    return HttpResponse("check terminal")


def check_book(request,url_string):

    book=Book.objects.get(slug=url_string)
    placeholder = ""
    values=[]

    user = request.user
    book_name=book.title
    authors=book.authors.all()
    publisher=book.publisher
    values=book
    # to=token.objects.filter(user_name=user)
    # for t in to:
    #     print(t.user_name)
    # #print(user.id)
    if not request.user.is_authenticated:
        messages.error(request,"You need to login inorder to issue a book")
        #return render(request,'bookissue/issue.html')
        return redirect('book:list')
        #return redirect('book:detail'+'/'+url_string)
        
    else:
        if book.no_of_copy_left==0:
            messages.error(request,"There is no stock available!")
            return redirect('book:list')
        else:
            return render(request, 'book/bookform2.html',{'user':user,'values':values})


def check_bookp(request,url_string):

    book=Book.objects.get(slug=url_string)
    placeholder = ""
    values=[]

    user = request.user
    book_name=book.title
    authors=book.authors.all()
    publisher=book.publisher
    values=book
    # to=token.objects.filter(user_name=user)
    # for t in to:
    #     print(t.user_name)
    # #print(user.id)
    if not request.user.is_authenticated:
        messages.error(request,"You need to login inorder to issue a book")
        #return render(request,'bookissue/issue.html')
        return redirect('book:list')
        #return redirect('book:detail'+'/'+url_string)
        
    else:
        if book.no_of_copy_left==0:
            messages.error(request,"There is no stock available!")
            return redirect('book:list')
        else:
            return render(request, 'book/bookformp2.html',{'user':user,'values':values})



import random
import time
def gen_token(request,booktoken):

    n=token.objects.all().last()

    book=Book.objects.get(slug=booktoken)
    # t0=time.time()
    # tokens=random.randint(1, 3910209312)

    # for t in at.token:
    #     if t == tokens:
    #         tokens=random.randint(1, 3910209312)
    if n:
        date=n.date
        if date==timezone.now:
            tokens=n.token+1
        else:
            tokens=1
    else:
        tokens=0

    messages.success(request,"Your token is {}".format(tokens))
    user1 = request.user
    user1.book_issued.add(book)
    #user=User.objects.filter(username=user1)
    token.objects.create(token=tokens,user_name=user1,book_name=book)
    #token.save()
    
    book.no_of_copy_left=book.no_of_copy_left-1
    book.save()
    
    return redirect('book:list')


def undo(request,booki):

    book=Book.objects.get(slug=booki)
    user = request.user
    token.objects.get(book_name=book,user_name=user).delete()
    user.book_issued.remove(book)
    #token.save()
    messages.error(request,"You have cancelled your order!")
    book.no_of_copy_left=book.no_of_copy_left+1
    book.save()
    return redirect('book:list')



