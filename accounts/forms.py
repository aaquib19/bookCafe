from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm

from accounts.models import Student,User,General,Teacher

from django.contrib.auth.forms import  UserChangeForm,PasswordChangeForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit,Field

User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','first_name','last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False # send confirmation email via signals
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ( 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


#
# class RegisterForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         #fields = ('first_name', 'email',) #'full_name',)
#         fields = ('email', 'first_name', 'last_name')
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(RegisterForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         user.is_active = False # send confirmation email via signals
#         # obj = EmailActivation.objects.create(user=user)
#         # obj.send_activation_email()
#         if commit:
#             user.save()
#         return user



class TeacherSignUpForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(TeacherSignUpForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].required = True
        
    class Meta(UserAdminCreationForm.Meta):
        model = User

    helper = FormHelper()
    helper.layout = Layout(
        Field('email', css_class='form-control '),
        Field('first_name', css_class='form-control'),
        Field('last_name', css_class='form-control'),
        Field('password1', css_class='form-control'),
        Field('password2', css_class='form-control'),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        )
    )

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_teacher = True
    #     if commit:
    #         user.save()
    #     return user


class generalSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(generalSignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True

    class Meta(UserAdminCreationForm.Meta):
        model = User

    helper = FormHelper()
    helper.layout = Layout(
        Field('email', css_class='form-control '),
        Field('first_name', css_class='form-control'),
        Field('last_name', css_class='form-control'),
        Field('password1', css_class='form-control'),
        Field('password2', css_class='form-control'),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        )
    )

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_general = True
    #     if commit:
    #         user.save()
    #     return user



class StudentSignUpForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(StudentSignUpForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].required = True

    class Meta(UserAdminCreationForm.Meta):
        model = User
        fields = ('email','first_name','last_name')

    helper = FormHelper()
    helper.layout = Layout(
        Field('email', css_class='form-control '),
        Field('first_name', css_class='form-control'),
        Field('last_name', css_class='form-control'),
        Field('password1', css_class='form-control'),
        Field('password2', css_class='form-control'),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        )
    )

    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_student = True
    #     user.save()
    #     #student = Student.objects.create(user=user)
    #     return user

class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
           # 'password'
        )

    helper = FormHelper()
    helper.layout = Layout(
        Field('email', css_class='form-control '),
        Field('first_name', css_class='form-control'),
        Field('last_name', css_class='form-control'),
        # Field('password1', css_class='form-control'),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white'),
        )

    )
        
class LoginForm(forms.Form):
    email = forms.EmailField(label="email")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Your username or password is incorrect")
        return self.cleaned_data

    def login(self, request):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        return user

    helper = FormHelper()
    helper.layout = Layout(
        Field('email', css_class='form-control '),
        Field('password', css_class='form-control'),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        )
    )

# class StudentInterestsForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ('interests', )
#         widgets = {
#             'interests': forms.CheckboxSelectMultiple
#         }

class GeneralCreationForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class GeneralExtraForm(ModelForm):
    class Meta:
        model = General
        fields = ('address','phone','pincode','city')

class StudentExtraForm(ModelForm):
    class Meta:
        model = Student
        fields = ('bio','college')

class TeacherExtraForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('department',)
