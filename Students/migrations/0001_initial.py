# Generated by Django 3.2 on 2021-06-01 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=30)),
                ('StudentRollNo', models.CharField(max_length=10, unique=True)),
                ('Standard', models.CharField(choices=[('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('9th', '9th'), ('10th', '10th')], max_length=5)),
            ],
        ),
    ]