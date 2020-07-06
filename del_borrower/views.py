from django.shortcuts import render,redirect

# Create your views here.
from borrower.models import token
from events.models import borrower_detail
from book.models import Book
from accounts.models import User
from django.utils import timezone
from django.contrib import messages


from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required

def disp_borrowers(request):
	context={"borrowers":borrower_detail.objects.all()}
	return render(request,"del_borrower/del.html",context)

def cal_fine(rdate,sdate):

	if rdate>sdate:
		days=rdate-sdate
		fine=(days.total_seconds()*5)/86400
	else:
		fine=0

	return fine




def del_borrower(request):

	if request.method=="POST":
		name=request.POST.get("borrow-id")
		book_name=request.POST.get("book_name")
	name1=User.objects.get(email=name)
	book_name1=Book.objects.get(title=book_name)
	b = borrower_detail.objects.get(name=name1,book_name=book_name1)
	user=b.name
	book=b.book_name
	rdate=timezone.now().date()
	sdate=b.submission_date
	book=Book.objects.get(id=book.id)
	# print(user,book,rdate,sdate)
	print(book)

	if b.pooled_users.all():
		name1.book_issued.remove(book)
		for p in b.pooled_users.all():
			p.book_issued.remove(book)

	else:

		name1.book_issued.remove(book)


	fine=cal_fine(rdate,sdate)

	b.delete()
	if fine:
		messages.error(request,"{} fine is Rs.{}".format(name1,fine))
		return redirect("del_borrower:disp_borrowers")
	else:
		return redirect("del_borrower:disp_borrowers")
