from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from bookcafe.utils import random_string_generator
from django.contrib.auth.decorators import login_required

@login_required
def payment(request):
    domain = request.META['HTTP_HOST']
    paypal_dict = {
    'business': request.user,
    'amount': '100',
    'item_name': 'Item_Name_xyz',
    'invoice': random_string_generator(),
    'notify_url': domain +'/paypal/',
    'return_url':domain +'/paypal-return/',
    'cancel_return': domain +'/paypal-cancel/',
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render_to_response('payment.html',{"form":form,'userid':paypal_dict['business'],'amount':paypal_dict['amount'],'book_name':paypal_dict['item_name']})

@csrf_exempt
def paypal_return(request):
    return render_to_response('paypal_return.html',{'post': request.POST,'get':request.GET})

@csrf_exempt
def paypal_cancel(request):
    return render_to_response('paypal_cancel.html',{'post': request.POST,'get':request.GET})
