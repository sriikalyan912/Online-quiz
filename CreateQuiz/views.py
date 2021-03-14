from django.shortcuts import render

from .forms import QuizForm

from .models import *

def create_quiz(request):

     if request.method == 'POST':

          quiz = dict(request.POST)

          quiz_name = quiz['Quiz_name'][0]
          quiz_model = Quiz(Quiz_name=quiz_name)

          quiz_model.save()
     
          for i in range(10):
               question_model = Questions(Quiz_name = quiz_model, 
               Question_no = i+1,
               Question = quiz['question'][i], 
               option_A = quiz['option_A'][i],
               option_B = quiz['option_B'][i],
               option_C = quiz['option_C'][i],
               option_D = quiz['option_D'][i],
               correct_option = quiz['correct_option'][i]
               )
               question_model.save()


     context = {
         'range' : list(range(1,11)),
         'form' : QuizForm,
    }
     return render(request, 'createquiz.html', context)
