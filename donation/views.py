from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import donation
# Create your views here.
def donate(request):

    #print("book issed by user",request.user.book_issued.all())
    # templates=loader.get_template('donate.html')
    # return HttpResponse(templates.render())
	return render(request,"donation/donate.html")

def adduser(request):

	if request.method=="POST":
		name=request.POST.get("name")
		email=request.POST.get("email")
		book_name=request.POST.get('book_name')

		donation.objects.create(name=name,emaild=email,bookname=book_name)


	return render(request,"donation/donate.html")

