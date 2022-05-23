from django.urls import path
from apps import views

urlpatterns = [

    path('index', views.index, name='index'),
    path('log', views.login, name='login'),
    path('login', views.authentic, name='authetic'),
    path('', views.home, name='home'),

    path('register', views.StudentRegister, name='StudentReg'),
    path('empregister', views.EmployeeRegister, name='employeReg'),

    path('empview', views.StudentTeachersView, name='StudentTeachersView'),
    path('indview', views.individualview, name='individualview'),
    path('view', views.StudentsView, name='StudentsView'),
    path('adminview', views.adminstudentview, name='adminstudentview'),

    path('EmployeeDelete/<int:id>', views.EmployeeDelete, name='EmployeeDelete'),
    path('EmployeeEdit/<int:id>', views.EmployeeEdit, name='EmployeeEdit'),
    path('EmployeeUpdate/<int:id>', views.EmployeeUpdate, name='EmployeeUpdate'),

    path('StudentDelete/<int:id>', views.StudentDelete, name='StudentDelete'),
    path('StudentEdit/<int:id>', views.StudentEdit, name='StudentEdit'),
    path('StudentUpdate/<int:id>', views.StudentUpdate, name='StudentUpdate'),
    path('StudentApprove/<int:id>', views.StudentApprove, name='StudentApprove'),
]
