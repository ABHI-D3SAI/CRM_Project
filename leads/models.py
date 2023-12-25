from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass 

class Leads(models.Model):

    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    Age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)