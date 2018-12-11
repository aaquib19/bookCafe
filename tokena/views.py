from django.shortcuts import render,redirect

# Create your views here.
from borrower.models import token
from events.models import borrower_detail

def disp_tokens(request):
	context={"tokens":token.objects.all()}
	return render(request,"tokena/ad.html",context)


def add_book(request,tokenNo):

	t=token.objects.get(token=tokenNo)
	user=t.user
	book=t.book
	date=t.date
	rdate=t.rdate
	t.deleted=True
	t.save()

	b=borrower_detail.objects.create(name=user,issue_date=date,submission_date=rdate)
	b.book_name.add(book)

	return redirect("tokena:disp_tokens")