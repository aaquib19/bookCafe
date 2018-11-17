from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView
from django.shortcuts import reverse
from django.contrib.auth.forms import  UserChangeForm,PasswordChangeForm

#import this for better redirection
# from django.utils.http import is_safe_url

# Create your views here.


from accounts.forms import LoginForm, EditProfileForm


#
# class RegisterView(CreateView):
#     form_class = RegisterForm
#     template_name = "accounts/register.html"
#     success_url = '/login/'
#
#


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





def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)



def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }

    #for redirection

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            print("error !!!")

    return render(request,"accounts/login.html",context)

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