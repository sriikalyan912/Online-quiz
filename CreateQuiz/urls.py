from django.urls import path
from .views import AvailableQuizzes, CreateQuiz, CreateQuestion, QuizCreated

urlpatterns = [
    path('availablequizzes/', AvailableQuizzes, name='availablequizzes'),
    path('createquiz/', CreateQuiz),
    path('createquestions/<int:id>/<int:no>', CreateQuestion),
    path('quizcreated/', QuizCreated, name='QuizCreated')
]