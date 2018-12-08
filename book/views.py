from rest_framework.views import APIView
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status


from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.views.generic import ListView,DetailView
from django.contrib import messages
from .models import Book
from borrower.models import token,pooled_token
from django.utils import timezone
# Create your views here.
from accounts.models import User



from accounts.models import User


class BookListView(ListView):
    template_name = "book/list.html"
    queryset = Book.objects.all()
    paginate_by = 9

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
            context['token'] = token.objects.filter(user=user)
        # Add in a QuerySet of all the books
        
        print(token.book)
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
    token.objects.create(token=tokens,user=user1,book=book)
    #token.save()
    
    book.no_of_copy_left=book.no_of_copy_left-1
    book.save()
    
    return redirect('book:list')


def gen_tokenp(request,booktoken):

    email2=request.POST.get("username2")
    print(email2)    
    email3=request.POST.get("username3")
    try :
        user2 = User.objects.get(email=email2)
        user3 = User.objects.get(email=email3)
    except:
        raise User.DoesNotExist("users does not exist")
    


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
    user2.book_issued.add(book)
    user3.book_issued.add(book)
    #user=User.objects.filter(username=user1)
    object1 =pooled_token.objects.create(token=tokens,main_user=user1,book=book)
    object1.pooled_user.add(user2)
    object1.pooled_user.add(user3)
    #token.save()
    object1.save()
    book.no_of_copy_left=book.no_of_copy_left-1
    book.save()
    
    return redirect('book:list')



def undo(request,booki):

    book=Book.objects.get(slug=booki)
    user = request.user
    token.objects.get(book=book,user=user).delete()
    user.book_issued.remove(book)
    #token.save()
    messages.error(request,"You have cancelled your order!")
    book.no_of_copy_left=book.no_of_copy_left+1
    book.save()
    return redirect('book:list')




class ListBookView(APIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    def get(self,request,format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)


    def post(self,request,format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailBookView(APIView):

    def get_object(self,pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        book =self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
