from django.urls import path
from . import views

urlpatterns= [
        
    path('students/',views.studentsView),
    path('students/<str:pk>/',views.studentDetailView),
    path('employees/',views.Employees.as_view()),
    path('employees/<str:pk>/',views.EmployeeDetailView.as_view()),
]