from django.shortcuts import redirect, render
from .models import Quiz, Questions
from django.contrib.auth.decorators import login_required

@login_required(login_url='/stafflogin')
def AvailableQuizzes(request):

    quizzes = list(Quiz.objects.all())
    
    context = {
        'quizzes' : quizzes
    }

    return render(request, 'availablequizzes.html', context)

@login_required(login_url='/stafflogin')
def CreateQuiz(request):

    quiz = Quiz()

    if request.method == 'POST':
        
        quizname = request.POST.get('QuizName')
        quizcreator = request.user
        duedate = request.POST.get('DueDate')

        quiz = Quiz(QuizName=quizname, QuizCreator=quizcreator, DueDate = duedate)

        quiz.save()

        return redirect(f'/createquestions/{quiz.QuizId}/0')

    context = {
        'staff' : request.user,
    }
    
    return render(request, 'createquiz.html', context)

@login_required(login_url='/stafflogin')
def CreateQuestion(request, id, no):
    
    
    if no < 10:
        quiz = Quiz.objects.get(QuizId=id)
        if request.method == 'POST':
            no += 1
            
            question = request.POST.get('Question')
            
            optionA = request.POST.get('OptionA')
            optionB = request.POST.get('OptionB')
            optionC = request.POST.get('OptionC')
            optionD = request.POST.get('OptionD')

            correctoption1 = request.POST.get('CorrectChoise1')
            correctoption2 = request.POST.get('CorrectChoise2')
            correctoption3 = request.POST.get('CorrectChoise3')

            question = Questions(
                QuizName=quiz, 
                Question=question, 
                OptionA=optionA, 
                OptionB=optionB, 
                OptionC=optionC, 
                OptionD=optionD,
                CorrectChoise1=correctoption1,
                CorrectChoise2=correctoption2,
                CorrectChoise3=correctoption3, 
                )
            question.save()

            return redirect(f'/createquestions/{id}/{no}')
        
        context = {
            
            'quizname':quiz.QuizName
        }
        return render(request, 'createquestion.html', context)

    else:
        return redirect('QuizCreated')

@login_required(login_url='/stafflogin')
def QuizCreated(request):
    return render(request, 'quizcreated.html')