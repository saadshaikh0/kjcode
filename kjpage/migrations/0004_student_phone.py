# Generated by Django 2.2.6 on 2020-06-02 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kjpage', '0003_student_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.IntegerField(default=0, max_length=11),
        ),
    ]
