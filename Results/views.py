from django.shortcuts import redirect, render
from CreateQuiz.models import Quiz
from Results.models import Results
from Students.models import Student

def QuizResults(request, QuizID):
    
    quiz = Quiz.objects.get(QuizId=QuizID)

    results = list(Results.objects.filter(Quiz=quiz))

    context = {
        'results':results,
        'quiz' : quiz.QuizName
    }

    return render(request, 'quizresults.html', context)

def Result(request, id):

    result = Results.objects.get(ResultId=id)
    context = {'result': result}
    return render(request, 'studentquizresult.html', context)