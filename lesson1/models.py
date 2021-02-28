from django.db import models

# Create your models here.
from django.db.models import SET_NULL

class Course(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField(default=0)
    university = models.TextField(null=True)


class Student(models.Model):
    course = models.ForeignKey(Course, null=True, on_delete=SET_NULL, related_name='count')
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name