from django.shortcuts import render
#from django.http import JsonResponse
from student.models import Student
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee
from django.http import Http404
# Create your views here.
#def studentsView(req):
#    students=Student.objects.all()
    ### Without using serializer
    #print(students)          # this will give err as it is not a list so we have to use serializer or do manual serialization
    #students_list=list(students.values())

    ### Using Serializer

@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        students=Student.objects.all()
        serializer= StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def studentDetailView(request,pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer= StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
         return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='DELETE':
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    


    ### Without Serializer
    # return JsonResponse(students_list, safe=False)


class Employees(APIView):
    def get(self,request):
        employees=Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # def put(self,request):
    #     serializer = EmployeeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self,request):
    #     Employee.delete()
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    

class EmployeeDetailView(APIView):
    def get_object(self,pk):
        try:
          employee=Employee.objects.get(pk=pk)
          return employee
        except Employee.DoesNotExist:
            raise Http404
        
    def get(self,request, pk):
        employee=self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK) 


    def put(self,request,pk):
        employee=self.get_object(pk)
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(employee, status=status.HTTP_201_CREATED)
        else:
            return Response(employee.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employee=self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)