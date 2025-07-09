from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    skills = [
        "HTML", "CSS", "Tailwind", "JavaScript", "React", "Python", "Django",
        "Solidity", "Ethereum", "Web3.js", "Git", "GitHub"
    ]
    return render(request, 'home.html', {'skills': skills})


def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # You can add email sending or form handling here
        pass
    return render(request, 'contact.html')
