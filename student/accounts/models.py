from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phno=models.CharField(max_length=10)  

class Staff(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=15)
    phno=models.CharField(max_length=10)

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()
    dep_image = models.ImageField()