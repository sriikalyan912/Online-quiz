from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=32, null=False)
    age = models.IntegerField(default=21)
    phone = models.BigIntegerField(null=True)
    