from django.db import models
from django.contrib.auth.models import User


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

class Ride(models.Model):
    ride_id = models.CharField(
        max_length=50,
        unique=True,
        db_index=True
    )

    driver = models.CharField(
        max_length=100,
        db_index=True
    )

    driver_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="rides",
        null=True,
        blank=True,
        db_index=True
    )

    status = models.CharField(
        max_length=20,
        db_index=True
    )

    fare = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.ride_id