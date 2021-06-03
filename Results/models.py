from django.db import models
from CreateQuiz.models import Quiz
from Students.models import Student

class Results(models.Model):
    ResultId = models.AutoField(primary_key=True)
    Quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    TimeTakenToFinish = models.CharField(max_length=8)
    TestTakenDate = models.DateTimeField(auto_now_add=True)
    Score = models.PositiveIntegerField()

    def __str__(self):
        return self.Student.StudentName