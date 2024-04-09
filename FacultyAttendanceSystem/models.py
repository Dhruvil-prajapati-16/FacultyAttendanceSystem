# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#Add Faculty_name
class Faculty(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

 #Add Faculty_username and password for that faculty   
class AdminCredentials(models.Model):
    faculty = models.OneToOneField(Faculty, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.faculty.name
    
#Timetable assin by admin to that faculty

class Semester(models.Model):
    name = models.CharField(max_length=120)
    start_date = models.DateField(verbose_name='start term date')
    end_date = models.DateField(verbose_name='end term date')
    
    def __str__(self):
        return f'{self.name}-{self.start_date}-{self.end_date}'
    
class Subject(models.Model):
    name = models.CharField(max_length=200, unique=True)
    short_name = models.CharField(max_length=200)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, related_name='subjects',null=True)

    def __str__(self):
        return self.name

class ClassDuration(models.Model):
    duration = models.CharField(max_length=20)
    duration_short_name = models.CharField(max_length=20)
    hours = models.IntegerField(null=True)
    minute = models.IntegerField(null=True)

    def __str__(self):
        return '{}'.format(self.duration)

class Room(models.Model):
    room_name = models.CharField('Room name', max_length=200)

    def __str__(self):
        return self.room_name

#main Timetable
class Timetable(models.Model):
    CLASS_TYPE_CHOICES = (
        ('lecture', 'lecture'),
        ('lab', 'lab')
    )
    class_type = models.CharField('Class Type', max_length=200, null = True, blank = True, choices=CLASS_TYPE_CHOICES, default='scheduled')
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL,null=True)
    faculty = models.ForeignKey(Faculty, verbose_name='faculty_id', null=True,on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, verbose_name='subject', related_name='subject',on_delete=models.SET_NULL,null=True)
    room = models.ForeignKey(Room, verbose_name='Room', related_name='room',on_delete=models.SET_NULL,blank= True,null= True)
    duration = models.ForeignKey(ClassDuration, related_name='class_definition_duration',on_delete=models.SET_NULL,null=True)
    create_date = models.DateTimeField('Class definition create date',auto_now_add=True,null=True)
    created_by_user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL, related_name='class_definition_creator')
    modified_date = models.DateTimeField('Class definition modified date',auto_now=True,null=True)
    modified_by_user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL, related_name='class_definition_modifier')
    
    def __str__(self):
        return f'{self.semester}-{self.subject.short_name}-{self.faculty}-{self.room}'

class TimeTableRollouts(models.Model):
    STATUSES_CHOICES = (
        ('scheduled', 'scheduled'),
        ('cancelled', 'cancelled'),
        ('break', 'break'),
        ('discontinued', 'discontinued'),
    )

    faculty = models.ForeignKey(Faculty, verbose_name='faculty_id', null=True,on_delete=models.SET_NULL)
    room = models.ForeignKey(Room,  null = True, blank = True,on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, null = True, blank = True , verbose_name='Subject',on_delete=models.SET_NULL)
    duration = models.ForeignKey(ClassDuration, null = True, blank = True, related_name='class_rollout',on_delete=models.SET_NULL)
    class_id = models.ForeignKey(Timetable, null = True, blank = True, related_name='class_rollout',on_delete=models.SET_NULL,verbose_name='Class definition')
    class_status = models.CharField('Class status', max_length=200, null = True, blank = True, choices=STATUSES_CHOICES, default='scheduled')
    class_attedance = models.BooleanField(default=False,verbose_name='Faculty Attedance')
    created_by = models.ForeignKey(Faculty, related_name='class_created_by',null=True,on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(Faculty, related_name='class_modified_by', null=True,on_delete=models.SET_NULL)
    create_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now, null=True)
    start_time = models.TimeField('Start time',null = True, blank = True)
    end_time = models.TimeField('End time',null = True, blank = True)
    class_date = models.DateField('Class date', null = True, blank = True)

    
    def __str__(self):
        subject = self.subject.name if self.subject else ""
        return "Class for: {} at {}".format(subject, self.class_date)
    

