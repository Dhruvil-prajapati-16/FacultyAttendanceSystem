# Generated by Django 5.0.4 on 2024-05-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacultyAttendanceSystem', '0013_holidayscheduler_eventscheduler'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='term_date',
            field=models.CharField(max_length=100, null=True, verbose_name='Term Date'),
        ),
    ]
