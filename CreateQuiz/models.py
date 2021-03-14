from django.contrib.admin import options
from django.db import models

class Quiz(models.Model):
    
    Quiz_name = models.CharField(max_length=10)


class Questions(models.Model):

    Quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    Question_no = models.IntegerField(null=True)
    
    Question = models.TextField()

    option_A = models.TextField()
    option_B = models.TextField()
    option_C = models.TextField()
    option_D = models.TextField()
    correct_option = models.CharField(max_length=1)