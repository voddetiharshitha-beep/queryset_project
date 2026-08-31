from django.db import models

# Create your models here.
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    marks = models.IntegerField()
    city = models.CharField(max_length=100)
    fees_paid = models.IntegerField(default=0)
    fees_total = models.IntegerField(default=10000)

    def __str__(self):
        return self.name