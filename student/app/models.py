from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    age = models.BigIntegerField()