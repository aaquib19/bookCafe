from django.shortcuts import render,redirect

# Create your views here.
from borrower.models import token
from events.models import borrower_detail

from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def disp_tokens(request):
	context={"tokens":token.objects.all()}
	return render(request,"tokena/ad.html",context)


def add_book(request,tokenNo):

	t=token.objects.get(token=tokenNo)
	

	user=t.user
	book=t.book
	date=t.date
	rdate=t.rdate


	if t.user2 and t.user3:
		user2=t.user2
		user3=t.user3
		b=borrower_detail.objects.create(name=user,book_name=book,issue_date=date,submission_date=rdate)
		b.pooled_users.add(user2)
		b.pooled_users.add(user3)

	else:	
		b=borrower_detail.objects.create(name=user,book_name=book,issue_date=date,submission_date=rdate)


	t.deleted=True
	t.save()
	print(rdate)
	# b.book_name.add(book)
	b.save()

	return redirect("tokena:disp_tokens")