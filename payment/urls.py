from django.urls import path
from . import views

app_name ='payment'
urlpatterns = [
    path('<int:pk>/',views.payment,name="payment"),
    path('paypal-return/',views.paypal_return,name='paypal_return'),
    path('paypal-cancel/',views.paypal_cancel,name="paypal_cancel"),
]
