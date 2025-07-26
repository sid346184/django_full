from django.shortcuts import render
from django.http import JsonResponse
from student.models import Student
# Create your views here.

def studentsView(req):
    students=Student.objects.all()
    #print(students)          # this will give err as it is not a list so we have to use serializer or do manual serialization
    students_list=list(students.values())
    return JsonResponse(students_list, safe=False)