from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView

#import this for better redirection
# from django.utils.http import is_safe_url

# Create your views here.


from .forms import LoginForm, RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = '/login/'




class LoginView(FormView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    success_url = "/"

    def form_valid(self, form):
        request = self.request
        #for advance redirecction
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        return super(LoginView, self).form_invalid(form)







# def login_page(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         "form":form
#     }
#
#     #for redirection
#
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#
#         user = authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect("/")
#         else:
#             print("error !!!")
#
#     return render(request,"accounts/login.html",context)
#
#
#
# User = get_user_model()
# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context={
#         "form":form
#     }
#
#     if form.is_valid():
#         print(form.cleaned_data)
#         username= form.cleaned_data.get("username")
#         email = form.cleaned_data.get("email")
#         password=form.cleaned_data.get("password")
#         new_user = User.objects.create_user(username,email,password)
#         print(new_user)
#
#     return render(request,"accounts/register.html",context)