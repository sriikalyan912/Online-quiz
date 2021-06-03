from django.contrib.auth import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StaffRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StaffLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']