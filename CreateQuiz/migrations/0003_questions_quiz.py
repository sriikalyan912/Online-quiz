# Generated by Django 3.1.7 on 2021-03-12 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CreateQuiz', '0002_auto_20210312_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quiz_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=100)),
                ('option_A', models.CharField(max_length=100)),
                ('option_B', models.CharField(max_length=100)),
                ('option_C', models.CharField(max_length=100)),
                ('option_D', models.CharField(max_length=100)),
                ('correct_option', models.CharField(max_length=100)),
                ('Quiz_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateQuiz.quiz')),
            ],
        ),
    ]
