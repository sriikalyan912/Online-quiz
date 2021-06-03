from django.urls import path
from .views import QuizzesOnline, QuizStartPage, TestPage, GetQuestions

urlpatterns = [
    path('quizzesonline/<int:roll>/', QuizzesOnline,name='quizzesonline'),
    path('quizzesonline/<int:roll>/<int:id>/<str:quiz>/', QuizStartPage,name='quizzesonline'),
    path('quizzesonline/<int:roll>/<int:id>/<str:quiz>/question/', TestPage),
    path('quizzesonline/<int:roll>/<int:id>/<str:quiz>/question/<int:questno>/', GetQuestions)
]
