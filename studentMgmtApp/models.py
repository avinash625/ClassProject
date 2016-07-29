from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Class(models.Model):
    className = models.TextField(max_length=30)
    classYear = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])



class Student(models.Model):
    studentName = models.TextField(max_length=30)
    studentYear = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    studentDept = models.TextField(max_length = 20)
    studentClass = models.ForeignKey(Class)


class Teacher(models.Model):
    teacherName = models.TextField(max_length=30)
    teacherDept = models.TextField(max_length=20)
    teacherClass = models.ManyToManyField(Class)