from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..decorators import student_required
from ..forms import  StudentSignUpForm,StudentExtraForm
from ..models import  Student, User

#
# class StudentSignUpView(CreateView):
#     model = User
#     form_class = StudentSignUpForm
#     template_name = 'registration/signup_form.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#
#         login(self.request, user)
#         return redirect('/')


def StudentSignup(request):
    if request.method == "POST":
        form1 = StudentSignUpForm(request.POST or None)
        form2 = StudentExtraForm(request.POST or None)
        if form1.is_valid() and form2.is_valid():
            ins = form1.save(commit=False)
            ins.save()
            email = ins.email
            #ins.is_active = True
            # print("form is valid")
            model_instance = form2.save(commit=False)
            #email = request.user.email
            user = User.objects.get(email=email)
            model_instance.user =user
            model_instance.save()
            # model_instance.timestamp = timezone.now()
            #model_instance.save()
            return redirect('/')
    else:
        print("form is invalid")

        form1 = StudentSignUpForm()
        form2 = StudentExtraForm()
    return render(request,'accounts/student_signup.html',{"form1":form1,"form2":form2})








