from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.views.generic import ListView,DetailView
from django.contrib import messages
from .models import Book,review
from borrower.models import token,pooled_token
from django.utils import timezone
from events.models import borrower_detail

from django.utils.timezone import utc

from datetime import timedelta
# Create your views here.
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
        slug = self.kwargs.get('slug')
        instance = Book.objects.get(slug=slug)
        if self.request.user.is_authenticated:
            user = self.request.user
            context['user'] = user
            context['token'] = token.objects.filter(user=user)
            context['review']=review.objects.filter(book=instance)
            context['borrower_detail']=borrower_detail.objects.filter(name=user,book_name=instance)
        # Add in a QuerySet of all the books
        
        print(token.book)
        return context


def test(request, url_string):
    print(url_string)
    return HttpResponse("check terminal")


def check_book(request,url_string):

    book=Book.objects.get(slug=url_string)

    user = request.user

    date=timezone.now().date()
    rdate=timezone.now()+timedelta(days=15)
    rdate=rdate.date()
    print(date,rdate)
    book_name=book.title
    authors=book.authors.all()
    publisher=book.publisher
    values=book
    if not request.user.is_authenticated:
        messages.error(request,"You need to login inorder to issue a book")
        return redirect('book:list')

    else:
        if book.no_of_copy_left==0:
            messages.error(request,"There is no stock available!")
            return redirect('book:list')
        else:
            return render(request, 'book/bookform2.html',{'user':user,'values':values,'date':date,'rdate':rdate})


def check_bookp(request,url_string):

    book=Book.objects.get(slug=url_string)

    placeholder = ""
    values=[]
    date=timezone.now().date()
    rdate=timezone.now()+timedelta(days=15)
    
    print(date,rdate)
    user = request.user
    values=book
    if not request.user.is_authenticated:
        messages.error(request,"You need to login inorder to issue a book")
        return redirect('book:list')

    else:
        if book.no_of_copy_left==0:
            messages.error(request,"There is no stock available!")
            return redirect('book:list')
        else:
            return render(request, 'book/bookformp2.html',{'user':user,'values':values,'date':date,'rdate':rdate})



def gen_token(request,booktoken):
    # print(request.POST)
    n=token.objects.all().last()
    # checkout=request.POST.get("returndate")
    rdate=timezone.now()+timedelta(days=15)
    book=Book.objects.get(slug=booktoken)
    # t0=time.time()
    # tokens=random.randint(1, 3910209312)

    # for t in at.token:
    #     if t == tokens:
    #         tokens=random.randint(1, 3910209312)
    # print ("----------------------")
    # print(timezone.now().date())
    # print(n.date.date())
    
    if n:
        date=n.date.date()
        if date==timezone.now().date():
            tokens=n.token+1
        else:
            tokens=1345
    else:
        date=timezone.now().date()
        tokens=32675

    messages.success(request,"Your token is {}".format(tokens))
    user1 = request.user
    user1.book_issued.add(book)
    #user=User.objects.filter(username=user1)
   
    token.objects.create(token=tokens,user=user1,book=book,rdate=rdate)
    #token.save()
    
    book.no_of_copy_left=book.no_of_copy_left-1
    book.save()
    
    return redirect('book:list')


def gen_tokenp(request,booktoken):

    email2=request.POST.get("username2")
    print(email2)    
    email3=request.POST.get("username3")
    rdate=timezone.now()+timedelta(days=15)
    try :
        user2 = User.objects.get(email=email2)
        user3 = User.objects.get(email=email3)
    except:
        raise User.DoesNotExist("users does not exist")
        # messages.error(request," doesn't exist")
        # return render(request, 'book/bookformp2.html')

    # if email2 not in User.objects.all():
    #     print("hiii")
    #     messages.error(request,"user doesn't exist")
    #     return redirect('book:list')
    # elif email3 not in User.objects.all():
    #     print("hiii222")
    #     messages.error(request,"user doesn't exist")
    #     return redirect('book:list')
    # else :
    #     user2 = User.objects.get(email=email2)
    #     user3 = User.objects.get(email=email3)

    n=token.objects.all().last()

    book=Book.objects.get(slug=booktoken)
    # t0=time.time()
    # tokens=random.randint(1, 3910209312)

    # for t in at.token:
    #     if t == tokens:
    #         tokens=random.randint(1, 3910209312)
    if n:
        date=n.date.date()
        if date==timezone.now().date():
            tokens=n.token+1
        else:
            tokens=1
    else:
        date=timezone.now().date()
        tokens=32675

    messages.success(request,"Your token is {}".format(tokens))
    user1 = request.user
    user1.book_issued.add(book)
    user2.book_issued.add(book)
    user3.book_issued.add(book)
    #user=User.objects.filter(username=user1)
    object1 =token.objects.create(token=tokens,user=user1,user2=user2,user3=user3,book=book,rdate=rdate)
    # object1.pooled_user.add(user2)
    # object1.pooled_user.add(user3)
    # #token.save()
    object1.save()
    book.no_of_copy_left=book.no_of_copy_left-1
    book.save()
    
    return redirect('book:list')



def undo(request,booki):

    book=Book.objects.get(slug=booki)
    user = request.user
    t=token.objects.get(book=book,user=user)
    # user=t.user
    user2=t.user2
    user3=t.user3
    t.delete()
    user.book_issued.remove(book)
    if user2 and user3:
        # user.book_issued.remove(book)
        user2.book_issued.remove(book)
        user3.book_issued.remove(book)

    #token.save()
    messages.error(request,"You have cancelled your order!")
    book.no_of_copy_left=book.no_of_copy_left+1
    book.save()
    return redirect('book:list')


def undop(request,booki):

    book=Book.objects.get(slug=booki)
    user = request.user
    #pooled_token.objects.get(book=book,user=user).delete()
    pooled_user=pooled_token.objects.get(book=book,user=user).pooled_user
    print(pooled_user)
    user.book_issued.remove(book)
    #token.save()
    messages.error(request,"You have cancelled your order!")
    book.no_of_copy_left=book.no_of_copy_left+1
    book.save()
    return redirect('book:list')


def reviews(request,bookn):
    book=Book.objects.get(slug=bookn)
    user = request.user

    s=request.POST.get("star")
    s=int(s)*20
    print(s)

    # if s=="1":
    #     print("ghj")
    # else:
    #     print("ert")
    # s2=request.POST.get("star2")
    # s3=request.POST.get("star3")
    # s4=request.POST.get("star4")
    # s5=request.POST.get("star5")

    text1=request.POST.get("text")

    if (review.objects.filter(book=book,user=user).exists()) :
        review.objects.get(book=book,user=user).delete()
        review.objects.create(rating=s,review=text1,book=book,user=user)
    else : 

        review.objects.create(rating=s,review=text1,book=book,user=user)

    messages.success(request,"your opinion is valuable for us , Thankyou!!")
    return redirect('book:list')
    
