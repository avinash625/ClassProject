from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Class(models.Model):
    className = models.TextField(max_length=30)
    classYear = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

    def __unicode__(self):
        return self.className



class Student(models.Model):
    studentName = models.TextField(max_length=30)
    studentYear = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    studentDept = models.TextField(max_length = 20)
    studentClass = models.ForeignKey(Class)

    def __unicode__(self):
        return self.studentName


class Teacher(models.Model):
    teacherName = models.TextField(max_length=30)
    teacherDept = models.TextField(max_length=20)
    classes = models.ManyToManyField(Class)

    def __unicode__(self):
        return self.teacherName


class  Test(models.Model):
    testName = models.TextField(max_length=30)
    testDate = models.DateField()
    testTeacher = models.ForeignKey(Teacher)
    testClass = models.ForeignKey(Class)

    def __unicode__(self):
        return self.testName

