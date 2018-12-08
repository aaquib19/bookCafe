from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

def home(request):

    #print("book issed by user",request.user.book_issued.all())
    return render(request,"home.html")


def payment(request):
    domain = request.META['HTTP_HOST']
    paypal_dict = {
    'business': 'aaquibniaz3600@gmail.com',
    'amount': '100',
    'item_name': 'Item_Name_xyz',
    'invoice': 'unique-invoice-00001',
    'notify_url': domain +'/paypal/',
    'return_url':domain +'/paypal-return/',
    'cancel_return': domain +'/paypal-cancel/',
    }

    form = PayPalPaymentsForm(initial=paypal_dict)

    return render_to_response('payment.html',{"form":form})

@csrf_exempt
def paypal_return(request):
    return render_to_response('paypal_return.html',{'post': request.POST,'get':request.GET})

@csrf_exempt
def paypal_cancel(request):
    return render_to_response('paypal_cancel.html',{'post': request.POST,'get':request.GET})

