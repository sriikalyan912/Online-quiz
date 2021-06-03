from django.forms import ModelForm, fields
from django.forms import Form
from .models import Quiz, Questions

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'


