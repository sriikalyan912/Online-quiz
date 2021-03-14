from django.urls import path

from .views import take_quiz, start_quiz, quiz_question, quiz_ans

urlpatterns = [
    path('', take_quiz, name='takequiz'),
    path('<str:quiz_name>/', start_quiz, name='start_quiz'),
    path('<str:quiz_name>/<int:question_no>', quiz_question),
    path('<str:quiz_name>/<int:question_no>/<str:User_Option>', quiz_ans),
]