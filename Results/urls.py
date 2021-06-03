from django.urls import path
from .views import QuizResults, Result

urlpatterns = [
    path('availablequizzes/<int:QuizID>/', QuizResults),
    path('result/<int:id>/', Result, name='result')
    
]