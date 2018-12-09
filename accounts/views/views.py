# from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib import messages
from rest_framework import viewsets
from accounts.models import User
from accounts.serializers import UserSerializer
from django.contrib.auth import authenticate, login, get_user_model, update_session_auth_hash
from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,View
from django.shortcuts import reverse
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
# from django.contrib.auth.forms import  UserChangeForm,PasswordChangeForm

#import this for better redirection
# from django.utils.http import is_safe_url


from accounts.models import EmailActivation
from accounts.forms import LoginForm, EditProfileForm
from django.utils.safestring import mark_safe

class AccountEmailActivateView(View):
    def get(self, request, key, *args, **kwargs):
        qs = EmailActivation.objects.filter(key__iexact=key)
        confirm_qs = qs.confirmable()
        if confirm_qs.count() == 1:
            obj = confirm_qs.first()
            obj.activate()
            messages.success(request, "Your email has been confirmed. Please login.")
            return redirect("login")
        else:
            activated_qs = qs.filter(activated=True)
            if activated_qs.exists():
                reset_link = reverse("password_reset")
                msg = """Your email has already been confirmed
                Do you need to <a href="{link}">reset your password</a>?
                """.format(link=reset_link)
                messages.success(request, mark_safe(msg))
                return redirect("login")
        return render(request, 'registration/activation-error.html', {})

    def post(self, request, *args, **kwargs):
        # create form to receive an email
        pass



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

class ListUserView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    def get(self,request,format=None):
        books = User.objects.all()
        serializer = UserSerializer(books,many=True)
        return Response(serializer.data)


    def post(self,request,format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

