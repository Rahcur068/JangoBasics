from django.shortcuts import get_object_or_404, render
from employees.models import Employee
from django.http import Http404,HttpResponse
# Create your views here.
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        'employee':employee,
    }
    #return HttpResponse(employee) -->will only detch the HTTP response page  of employee
    return render(request,'employee_detail.html',context) #will only render for the given employee