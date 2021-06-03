from django.db.models import fields
from django.forms import ModelForm
from .models import Student

class StudentRegisterForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class StudentLoginForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'