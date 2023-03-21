from django.db import models

# Create your models here.
class Task(models.Model):
	tname = models.CharField(max_length=10)
	tDetails = models.CharField(max_length=100)
	
class CompletedTask(models.Model):
	ctname = models.CharField(max_length=10)
	ctDetails = models.CharField(max_length=100)