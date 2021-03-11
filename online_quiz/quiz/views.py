from django.http import HttpResponse
from django.shortcuts import render

from .models import Quiz

def index(request):
    obj = Quiz.objects.get(id=2)
    context = {
        'Obj' : obj
    }
    return render(request, 'home.html', context)

def contacts(request):
    my_contactes = {
        'name' : 'Srinivas Kalyan',
        'phone' : '9384488592',
        'mail' : 'sriikalyan18@gmail.com'
    }
    return render(request, 'contacts.html', my_contactes)