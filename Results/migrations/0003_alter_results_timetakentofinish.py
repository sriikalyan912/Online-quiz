# Generated by Django 3.2 on 2021-06-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Results', '0002_auto_20210602_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='TimeTakenToFinish',
            field=models.CharField(max_length=8),
        ),
    ]