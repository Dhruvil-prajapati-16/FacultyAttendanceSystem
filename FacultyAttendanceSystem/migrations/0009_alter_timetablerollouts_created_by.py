# Generated by Django 5.0.4 on 2024-04-10 06:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FacultyAttendanceSystem', '0008_timetable_end_time_timetable_start_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetablerollouts',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
