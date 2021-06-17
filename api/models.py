from django.db import models

# Create your models here.

class Emp(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    salary = models.IntegerField()
    DOJ = models.DateField()
