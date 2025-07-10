from django.shortcuts import render
from django.http import HttpResponse
from employee.models import Employee

def home(request):
    skills = [
        "HTML", "CSS", "Tailwind", "JavaScript", "React", "Python", "Django",
        "Solidity", "Ethereum", "Web3.js", "Git", "GitHub"
    ]
    return render(request, 'home.html', {'skills': skills})


def about(request):
    return render(request, 'about.html')

def contact(request):
    employee = Employee.objects.all() 
    context = {'employee': employee
    } 
    if request.method == 'POST':

        pass
    return render(request, 'contact.html', context)
