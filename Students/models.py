from django.db import models
from django.db.models.enums import Choices

class Student(models.Model):
    STANDARD = (
        ('5th','5th'),
        ('6th', '6th'),
        ('7th', '7th'),
        ('9th', '9th'),
        ('10th','10th')
        )
    StudentName = models.CharField(max_length=30)
    StudentRollNo = models.CharField(max_length=10, unique=True)
    Standard = models.CharField(max_length=5, choices=STANDARD, null=False)

    def __str__(self):
        return self.StudentName
