from ..models import Employee
from rest_framework.response import Response

def upsertEmployee(self, request):

    try:
        employee = Employee.objects.get(id=request["id"])
        employee.name = request["name"]
        employee.department = request["department"]
        employee.city = request["city"]
        employee.save()

        employee_details = {"id": employee.id,
                                "name":employee.name,
                                "department":employee.department,
                                "city":employee.city
                                }
        return Response({'Message':'Employee', 'Employee':employee_details})

    except:
        Employee.objects.create(id=request["id"],
                                name=request["name"],
                                department=request["department"],
                                city=request["city"],
                                )


        employee = Employee.objects.all().filter(id=request["id"]).values()
        return Response({'Message':'New Employee added', 'Employee':employee})

def deleteEmployee(self, request):

    employee = Employee.objects.get(id=request['id'])
    employee.delete()
    
    return Response({'Message':'Employee Deleted'})

def listEmployee(self, request):

    if "id" in request:
            employee = Employee.objects.get(id=request["id"])
            employee_details = {"id": employee.id,
                                "name":employee.name,
                                "department":employee.department,
                                "city":employee.city
                                }
            return Response({'Message':'Employee', 'Employee':employee_details})

    else:
        allemployees = Employee.objects.all().values()
        return Response({'Message':'List of Employees', 'Employees List':allemployees})