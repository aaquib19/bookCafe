import profile

from django.urls import path,include,re_path
#from . import views

from .views import home1, students, teachers

from .views.students import StudentSignUpView
from .views.teachers import TeacherSignUpView
from .views import views
urlpatterns = [
path('', home1.home, name='home'),

    path('signup/', home1.SignUpView.as_view(),name="signup_all"),
    path('signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
    path('profile/', views.view_profile, name='view_profile'),
    #re_path(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),


]