from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def students(req):
    students=[
        {'id':1, 'name':'AMAN', 'gender':'male','isPresent':True}
    ]
    return HttpResponse(students)
