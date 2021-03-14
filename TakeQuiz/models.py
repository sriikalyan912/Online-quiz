from django.db import models

class Student(models.Model):
    Student_name = models.CharField(max_length=30)
    quiz_name = models.CharField(max_length=30,blank=True)
    Score = models.IntegerField(blank=True)
    time_taken = models.CharField(max_length=5,blank=True)