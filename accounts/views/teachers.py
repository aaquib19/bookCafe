# from django.contrib import messages
# from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
# from django.db import transaction
# from django.db.models import Avg, Count
# from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
# from django.urls import reverse, reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
#                                   UpdateView)

from ..decorators import teacher_required
from ..forms import TeacherSignUpForm,TeacherExtraForm
#from ..models import Answer, Question, Quiz
from ..models import  User



def TeacherSignup(request):
    if request.method == "POST":
        form1 = TeacherSignUpForm(request.POST or None)
        form2 = TeacherExtraForm(request.POST or None)
        if form1.is_valid() and form2.is_valid():
            ins = form1.save(commit=False)
            ins.is_teacher = True

            ins.save()
            email = ins.email
            model_instance = form2.save(commit=False)
            user = User.objects.get(email=email)
            model_instance.user =user
            model_instance.save()
            return redirect('/')
    else:
        print("form is invalid")

        form1 = TeacherSignUpForm()
        form2 = TeacherExtraForm()
    return render(request,'accounts/student_signup.html',{"form1":form1,"form2":form2})


