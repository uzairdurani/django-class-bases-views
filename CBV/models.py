from audioop import maxpp
from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(null=True)