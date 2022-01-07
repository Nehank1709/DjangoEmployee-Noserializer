from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .API import ApiEmployee

# Create your views here.
# class EmployeeApiView(APIView):

#     def get(self, request):
#         allemployees = Employee.objects.all().values()
#         return Response({'Message':'List of Employees', 'Employees List':allemployees})

#     def post(self,request):

#         Employee.objects.create(id=request.data["id"],
#                                 name=request.data["name"],
#                                 department=request.data["department"],
    #                             city=request.data["city"],
    #                             )


    #     employee = Employee.objects.all().filter(id=request.data["id"]).values()
    #     return Response({'Message':'New Employee added', 'Employee':employee})

    # def delete(self,request):

    #     employee = Employee.objects.get(id=request.data['id'])
    #     employee.delete()
    
    #     return Response({'Message':'Employee Deleted'})


class UpsertEmployee(APIView):
    def put(self, request):

        response_post = ApiEmployee.upsertEmployee(self,request.data)
        return response_post

class DeleteEmployee(APIView):
    def post(self, request):

        response_delete = ApiEmployee.deleteEmployee(self,request.data)
        return response_delete

class ListEmployee(APIView):
    def post(self, request):

        response_list = ApiEmployee.listEmployee(self,request.data)
        return response_list
