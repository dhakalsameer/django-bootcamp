from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Employee
# Create your views here.
def employee_details(request, pk):
    try:
        employee= Employee.objects.get(pk=pk)
        context = {
            'employee': employee
        }
    except:
        raise Http404("Employee not found")
    return render(request, 'employee_details.html')