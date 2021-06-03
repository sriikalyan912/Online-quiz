from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .forms import StudentLoginForm, StudentRegisterForm
from .models import Student

def checkstudent(request, studentform):
    
    studentname = request.POST.get('StudentName')
    studentroll = request.POST.get('StudentRollNo')
    standard = request.POST.get('Standard')

    StudentObject = Student.objects.filter(StudentRollNo__exact = studentroll)

    if StudentObject != None:
        Stu = StudentObject[0]

        if(Stu.StudentName == studentname):
            if(Stu.Standard == standard):
                return True
    else:
        False


def StudentLogin(request):
    studentform = StudentLoginForm()

    if request.method == 'POST':
        
        studentform = StudentLoginForm(request.POST)

        if checkstudent(request, studentform):
            roll = request.POST.get('StudentRollNo')
            return redirect('quizzesonline', roll = roll)
        else:
            
            return JsonResponse({'loginstatus': 0})

    context = {
        'Student':studentform
        }

    return render(request, 'studentlogin.html', context)

def StudentRegistration(request):
    studentform = StudentRegisterForm()

    if request.method == 'POST':
        studentform = StudentRegisterForm(request.POST)
        if studentform.is_valid():
            studentform.save()

            return redirect('StudentLogin')
    context = {
        'Student':studentform
        }
    return render(request, 'studentregistration.html', context)