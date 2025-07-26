from django.shortcuts import render
#from django.http import JsonResponse
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def studentsView(req):
    students=Student.objects.all()
    ### Without using serializer
    #print(students)          # this will give err as it is not a list so we have to use serializer or do manual serialization
    #students_list=list(students.values())

    ### Using Serializer

    def studentsView(request):
        if request.method == 'GET':
            students=Student.objects.all()
            serializer= StudentSerializer(students,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

    ### Without Serializer
    # return JsonResponse(students_list, safe=False)