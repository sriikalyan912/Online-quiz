# Generated by Django 3.2 on 2021-06-01 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateQuiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='CorrectChoise2',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='CorrectChoise3',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]