from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .form import StaffRegisterForm, StaffLoginForm


def StaffLogin(request):

    if request.method == 'POST':
        stafform = StaffLoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            return redirect('availablequizzes')
    
    return render(request, 'stafflogin.html')

def StaffRegister(request):
    stafform = StaffRegisterForm()

    if request.method == 'POST':
        stafform = StaffRegisterForm(request.POST)

        if stafform.is_valid():
            stafform.save()

            return redirect('stafflogin')

    context = {
        'Staff' : stafform
    }

    return render(request, 'staffregister.html', context)

def Logout(request):
    logout(request)
    return redirect('stafflogin')