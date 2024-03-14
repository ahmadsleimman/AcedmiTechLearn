from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    MAJOR = (
        ('Maths', 'Maths'),
        ('Physics', 'Physics'),
        ('Info', 'Info'),
        ('Biology', 'Biology'),
        ('Chemistry', 'Chemistry'),
        ('Bio-Chemistry', 'Bio-Chemistry'),
    )

    LANGUAGE = (
        ('Frensh', 'Frensh'),
        ('English', 'English'),
    )

    YEAR = (
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
    )

    name = models.CharField(max_length=40, verbose_name='Name')
    major = models.CharField(choices=MAJOR, max_length=20, verbose_name='Major')
    language = models.CharField(choices=LANGUAGE, max_length=10, verbose_name='Language')
    year = models.CharField(choices=YEAR, max_length=10, verbose_name='Year')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        ordering = ['-created']
        verbose_name = "Student"
        verbose_name_plural = "Students"
        db_table = 'Student'


class Teacher(models.Model):
    name = models.CharField(max_length=40, verbose_name='Name')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        ordering = ['-created']
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        db_table = 'Teacher'


class Course(models.Model):
    MAJOR = (
        ('Maths', 'Maths'),
        ('Physics', 'Physics'),
        ('Info', 'Info'),
        ('Biology', 'Biology'),
        ('Chemistry', 'Chemistry'),
        ('Bio-Chemistry', 'Bio-Chemistry'),
    )
    YEAR = (
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
    )
    SEMESTER = (
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2'),
    )
    name = models.CharField(max_length=30, verbose_name='Course Name')
    major = models.CharField(choices=MAJOR, max_length=20, verbose_name='Major')
    year = models.CharField(choices=YEAR, max_length=10, verbose_name='Year')
    semester = models.CharField(choices=SEMESTER, max_length=15, verbose_name='Semester')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        ordering = ['-created']
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        db_table = 'Course'


class Inbox(models.Model):
    name = models.CharField(max_length=45, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=45, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    isFeedback = models.BooleanField(verbose_name='Is Feedback', default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "Inbox"
        verbose_name_plural = "Inboxes"
        db_table = 'Inbox'

    def __str__(self):
        return f"{self.id}"
