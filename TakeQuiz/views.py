from django.shortcuts import render

from django.http import JsonResponse

from CreateQuiz.models import Quiz, Questions

def take_quiz(request):
    available_quizzes = Quiz.objects.all()
    
    return render(request, 'quizAvailable.html', { 'quizzes':available_quizzes })

def start_quiz(request, quiz_name):
    quiz = Quiz.objects.get(Quiz_name = quiz_name)
    quiz_questions = Questions.objects.filter(Quiz_name = quiz)
    
    context = {
        'quiz' : quiz,
        'questions': quiz_questions
    }
    
    return render(request, 'test.html', context)



def quiz_question(request, quiz_name, question_no):

    quiz = Quiz.objects.get(Quiz_name = quiz_name)

    question = Questions.objects.get(Quiz_name = quiz, Question_no = question_no)

    context = {
        'question' : question,
        'quiz_name' : quiz_name
    }

    return render(request, 'test.html', context)

def quiz_ans(request,quiz_name, question_no, User_Option):

    quiz = Quiz.objects.get(Quiz_name = quiz_name)

    Correct_option = Questions.objects.get(Quiz_name = quiz, Question_no = question_no).correct_option
    return JsonResponse({ 'is_correct' : Correct_option == User_Option})
