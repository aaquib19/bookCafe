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


def del_borrower(request):

	if request.method=="POST":
		name=request.POST.get("borrow-id")
	name1=User.objects.get(email=name)
	b = borrower_detail.objects.get(name=name1)
	user=b.name
	book=b.book_name
	rdate=timezone.now().date()
	sdate=b.submission_date
	# print(user,book,rdate,sdate)
	print(book)
	book=Book.objects.get(id=book.id)

	name1.book_issued.remove(book)

	if rdate>sdate:
		days=rdate-sdate
		fine=(days.total_seconds()*5)/86400
	else:
		fine=0

	b.delete()
	if fine:
		messages.error(request,"{} fine is Rs.{}".format(name1,fine))
		return render(request,"del_borrower/del.html")
	else:
		return render(request,"del_borrower/del.html")
