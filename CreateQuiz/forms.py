from CreateQuiz.models import Questions
from django import forms
from django.forms.fields import CharField

class QuizForm(forms.Form):
    Quiz_name = forms.CharField(label='Quiz Name')

class QuizQuestionsForm(forms.Form):
    Question = forms.CharField(label='Question')

    option_A = forms.CharField()
    option_B = forms.CharField()
    option_C = forms.CharField()
    option_D = forms.CharField()

    correct_option = forms.CharField(max_length=1)
