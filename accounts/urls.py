
from django.urls import path,include
#from . import views

from .views import home1, students, teachers

from .views.students import StudentSignUpView
from .views.teachers import TeacherSignUpView
from .views.views import LoginView
urlpatterns = [
path('', home1.home, name='home'),

    path('login/',LoginView.as_view(), name="signup_all"),

    path('signup/', home1.SignUpView.as_view(),name="signup_all"),
    path('signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),

]