# Generated by Django 3.1.7 on 2023-02-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2001-10-17'),
            preserve_default=False,
        ),
    ]
