from django.db import models


# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=20)


class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    phone = models.IntegerField()
    emp_code = models.CharField(max_length=10)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class State(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class User(models.Model):
    fullname = models.CharField(max_length=50)
    phone = models.IntegerField()
    emp_code = models.CharField(max_length=10)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
