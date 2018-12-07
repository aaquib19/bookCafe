from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

def home(request):

    #print("book issed by user",request.user.book_issued.all())
    return render(request,"home.html")


def payment(request):
    args = {}
    paypal_dict = {
    'business': 'narainmukul98@gmail.com',
    'amount': '100',
    'item_name': 'Item_Name_xyz',
    'invoice': 'unique-invoice-00001',
    'notify_url': '127.0.0.1:8000/a-very-hard-url/',
    'return_url':'127.0.0.1:8000/paypal-return/',
    'cancel_return': '127.0.0.1:8000/paypal-cancel/',
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    args['form'] =form

    return render_to_response('payment.html',args)

@csrf_exempt
def paypal_return(request):
    args = {'post': request.POST,'get':request.GET}
    return render_to_response('paypal_cancel.html',args)

@csrf_exempt
def paypal_cancel(request):
    args = {'post': request.POST,'get':request.GET}
    return render_to_response('paypal_cancel.html',args)

