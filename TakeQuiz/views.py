from Results.models import Results
from django.http.response import JsonResponse
from django.shortcuts import render
from CreateQuiz.models import Questions, Quiz
from Students.models import Student

def QuizzesOnline(request, roll):
    quizzes = list(Quiz.objects.all())
    
    context = {
        'studentroll':roll,
        'quizzes' : quizzes
    }
    return render(request, 'quizzesonline.html', context)

def QuizStartPage(request, roll, id, quiz):
    quiz = Quiz.objects.get(QuizId=id)
    context = {
        'studentroll':roll,
        'quiz':quiz
    }
    return render(request, 'quizstartpage.html', context)

def TestPage(request, roll, id, quiz):
    context={
        'studentroll':roll,
        'quiz':quiz
    }
    return render(request, 'testpage.html', context)


def GetQuestions(request, roll, id, quiz, questno):
    quiz = Quiz.objects.get(QuizId=id)

    if(questno < 10):
        questions = list(Questions.objects.filter(QuizName=quiz))
        question = questions[questno]

        answers = {'A':False, 'B':False, 'C':False, 'D':False}
        
        answers[question.CorrectChoise1] = True
        
        if question.CorrectChoise2 != None:
            answers[question.CorrectChoise2] = True
        
        if question.CorrectChoise3 != None:
            answers[question.CorrectChoise3] = True


        context = {
            'question' : question.Question,
            'options' : [question.OptionA, question.OptionB, question.OptionC, question.OptionD],
            'Answers' : answers
        }

        return JsonResponse(context)

    else:
        student = Student.objects.get(StudentRollNo=roll)
        timetaken = request.POST.get('timetaken')
        score = request.POST.get('score')

        result = Results(Quiz=quiz, Student=student, TimeTakenToFinish=timetaken, Score=score)
        result.save()
        return JsonResponse({
            'location' : f'/result/{result.ResultId}/'
        })