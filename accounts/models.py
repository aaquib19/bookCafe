from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager
)


from book.models import Book
#AUTH_USER_MODEL
USER_TYPE_CHOICES=(
    ('General','General'),
    ('Student','Student'),
    ('Teacher','Teacher'),
)

class UserManager(BaseUserManager):
    def create_user(self,email,first_name=None,password=None,is_active=True,is_staff=False,is_admin=False):
        if not email:
            raise ValueError("users must have email address")
        if not password:
            raise ValueError("users must have a password")
        user_obj = self.model(
            email = self.normalize_email(email),
            first_name=first_name
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.active= is_active
        user_obj.admin = is_admin

        user_obj.save(using=self._db)
        return user_obj

    # def create_stffuser
    def create_staffuser(self,email,first_name=None,password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self,email,first_name=None,password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            password=password,
            is_staff=True,
            is_admin=True
        )



class User(AbstractBaseUser):
    username = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(unique=True,max_length=255)
    first_name   = models.CharField(max_length=255, blank=True, null=True)
    last_name   = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    book_issued = models.ManyToManyField(Book,blank=True)
    #user_type=models.CharField(max_length=6,choices=USER_TYPE_CHOICES,blank=True,null=True)
    is_student = models.BooleanField(default=False)
    is_general = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    # department = models.CharField(max_length=255)
    # address = models.CharField(max_length=255)
    # phone = models.IntegerField(null=True,blank=True)
    # pincode = models.IntegerField(null=True,blank=True)
    # city = models.CharField(max_length=255)


    USERNAME_FIELD = 'email'
    #email and password field are required by default

    REQUIRED_FIELDS = []


    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + self.last_name
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True


    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    # @property
    # def is_active(self):
    #     return  self.active


from django.contrib.auth.models import AbstractUser
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #dob = models.DateField(null=True,blank=True)
    bio  =models.TextField(null=True,blank=True)
    college = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.user.email)


class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    department = models.CharField(max_length=255)


class General(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.IntegerField(null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    city = models.CharField(max_length=255)

