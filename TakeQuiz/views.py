from django.shortcuts import render

from django.http import JsonResponse, response

from .form import StudentForm

from CreateQuiz.models import Quiz, Questions

from .models import Student


def take_quiz(request):
    available_quizzes = Quiz.objects.all()
    
    return render(request, 'quizAvailable.html', { 'quizzes':available_quizzes })

def start_quiz(request, quiz_name):
    student = StudentForm(request.POST or None)

    context = {
        'quiz_name' : quiz_name,
        'form':student
    }
    

    return render(request, 'startQuiz.html', context )

def quiz(request, quiz_name,question_no=1):
    
    if request.method == 'POST':
        student_name = request.POST.get('name')
        print(student_name)
    

    quiz = Quiz.objects.get(Quiz_name = quiz_name)

    question = Questions.objects.get(Quiz_name = quiz, Question_no = question_no)
    
    context = {
        'quiz_name' : quiz_name,
        'question':question,
        'student_name' : student_name
        } 
    return render(request, 'test.html', context)

def quiz_question(request, quiz_name, question_no):

    quiz = Quiz.objects.get(Quiz_name = quiz_name)

    question = Questions.objects.get(Quiz_name = quiz, Question_no = question_no)

    context = {
        'question_no': question.Question_no,
        'question' : question.Question,
        'option_A' : question.option_A,
        'option_B' : question.option_B,
        'option_C' : question.option_C,
        'option_D' : question.option_D,
    }


    
    return JsonResponse(context)

def quiz_ans(request,quiz_name, question_no, User_Option):

    quiz = Quiz.objects.get(Quiz_name = quiz_name)

    Correct_option = Questions.objects.get(Quiz_name = quiz, Question_no = question_no).correct_option

    context = {
        'is_correct' : Correct_option == User_Option,
        'Correct_option' : Correct_option
    }

    return JsonResponse(context)

def finishTest(request, quiz_name, stu_name, Score_and_Timetaken):
    
    Score, Timetaken = Score_and_Timetaken.split('&')
    Save_test = Student.objects.create(Student_name = stu_name, quiz_name = quiz_name, Score = Score, time_taken = Timetaken)
    
    Save_test.save()
    context = {
        'student_name' : stu_name,
        'quiz_name' : quiz_name,
        'score' : Score.split(':'),
        'timetaken' : Timetaken
    }

    return JsonResponse(context)