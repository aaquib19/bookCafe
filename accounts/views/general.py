# from django.contrib import messages
# from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
# from django.db import transaction
# from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
# from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.generic import CreateView, ListView, UpdateView
#
# from ..decorators import general_required
from ..forms import  generalSignUpForm,GeneralExtraForm
from ..models import User


def GeneralSignup(request):
    if request.method == "POST":
        form1 = generalSignUpForm(request.POST or None)
        form2 = GeneralExtraForm(request.POST or None)
        if form1.is_valid() and form2.is_valid():
            ins = form1.save(commit=False)
            ins.is_general = True
            ins.is_active = False
            ins.save()

            email = ins.email
            model_instance = form2.save(commit=False)
            user = User.objects.get(email=email)
            model_instance.user =user
            model_instance.save()
            return redirect('/')
    else:
        print("form is invalid")

        form1 = generalSignUpForm()
        form2 = GeneralExtraForm()
    return render(request,'accounts/generalsignup.html',{"form1":form1,"form2":form2})












