from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=122, null=True)
    Password = models.CharField(max_length=122)
    
class Signup(models.Model):
    username1 = models.CharField(max_length=122, null=True)
    email1 = models.CharField(max_length=122, null=True)
    password = models.CharField(max_length=122, null=True)
    comform = models.CharField(max_length=122, null=True)
    