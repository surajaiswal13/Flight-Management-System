from django.db import models

# Create your models here.

class UserTest(models.Model):

    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    # city = 

class City(models.Model):
    name = models.CharField(max_length=6)
    users = models.ManyToManyField(UserTest)

class State(models.Model):
    name = models.CharField(max_length=10)
    users = models.ManyToManyField(UserTest)