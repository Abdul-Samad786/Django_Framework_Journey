from django.db import models

# Create your models here.

class Profile(models.Model):
    bio=models.TextField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    