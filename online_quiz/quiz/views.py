from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home.html', {})

def contacts(request):
    my_contactes = {
        'name' : 'Srinivas Kalyan',
        'phone' : '9384488592',
        'mail' : 'sriikalyan18@gmail.com'
    }
    return render(request, 'contacts.html', my_contactes)