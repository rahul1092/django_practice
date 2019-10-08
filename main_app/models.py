from django.db import models
from .choices import SUBJECTS

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Marks(models.Model):
    subject = models.CharField(max_length=20, choices=SUBJECTS)
    marks = models.FloatField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
