from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    