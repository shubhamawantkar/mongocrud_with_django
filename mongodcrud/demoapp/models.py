from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=10)
    desc = models.CharField(max_length=100)
    