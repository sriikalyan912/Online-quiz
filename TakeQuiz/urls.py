from django.urls import path

from .views import *

urlpatterns = [
    path('', take_quiz, name='takequiz'),
    path('<str:quiz_name>/', start_quiz, name='start_quiz'),
    path('<str:quiz_name>/test/', quiz),
    path('<str:quiz_name>/test/<int:question_no>', quiz_question),
    path('<str:quiz_name>/test/<int:question_no>/<str:User_Option>', quiz_ans),
    path('<str:quiz_name>/test/finishtest/<str:stu_name>/<str:Score_and_Timetaken>', finishTest, name='finishTest'),
]