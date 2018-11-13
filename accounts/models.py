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
    def create_user(self,email,full_name=None,password=None,is_active=True,is_staff=False,is_admin=False):
        if not email:
            raise ValueError("users must have email address")
        if not password:
            raise ValueError("users must have a password")
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name=full_name
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.active= is_active
        user_obj.admin = is_admin

        user_obj.save(using=self._db)
        return user_obj

    # def create_stffuser
    def create_staffuser(self,email,full_name=None,password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self,email,full_name=None,password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )



class User(AbstractBaseUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True,max_length=255)
    full_name   = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    book_issued = models.ManyToManyField(Book)
    user_type=models.CharField(max_length=6,choices=USER_TYPE_CHOICES,blank=True,null=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    #email and password field are required by default

    REQUIRED_FIELDS = []


    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
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
    @property
    def is_active(self):
        return  self.active


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    # interests = models.ManyToManyField(Subject, related_name='interested_students')

    # def get_unanswered_questions(self, quiz):
    #     answered_questions = self.quiz_answers \
    #         .filter(answer__question__quiz=quiz) \
    #         .values_list('answer__question__pk', flat=True)
    #     questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
    #     return questions

    def __str__(self):
        return self.user.username


# class TakenQuiz(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
#     score = models.FloatField()
#     date = models.DateTimeField(auto_now_add=True)


# class StudentAnswer(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')


