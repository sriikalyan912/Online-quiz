import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.lookups import Transform

class Quiz(models.Model):
    QuizId = models.AutoField(primary_key=True, editable=False)
    QuizName = models.CharField(max_length=50)
    QuizCreator = models.ForeignKey(User, on_delete=models.CASCADE)
    DateOfCreation = models.DateTimeField(auto_now_add=True)
    DueDate = models.DateTimeField()

    def __str__(self):
        return self.QuizName

class Questions(models.Model):
    
    QuizName = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    Question = models.TextField()

    OptionA = models.TextField()
    OptionB = models.TextField()
    OptionC = models.TextField()
    OptionD = models.TextField()

    CorrectChoise1 = models.CharField(max_length=1)
    CorrectChoise2 = models.CharField(max_length=1,null=True, blank=True)
    CorrectChoise3 = models.CharField(max_length=1,null=True, blank=True)

    def __str__(self):
        return self.Question
