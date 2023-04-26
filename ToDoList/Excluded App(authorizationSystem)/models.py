from django.db import models

# Create your models here.
class Licenses(models.Model):
    max_user = models.PositiveIntegerField()
    max_active = models.PositiveIntegerField()