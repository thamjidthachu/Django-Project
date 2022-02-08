from django.db import models

# Create your models here.

class Students(models.Model):
    First_Name = models.CharField(max_length=10)
    Last_Name = models.CharField(max_length=10)
    Age = models.IntegerField()
    Address = models.CharField(max_length=20)
    Contacts = models.IntegerField()
    Email = models.EmailField()
    username = models.CharField(max_length=10)
    password =models.CharField(max_length=10)
    # status = models.IntegerField(null=True,default=0)
    status = models.CharField(max_length=10,null=True,default="No")



class Employees(models.Model):
    First_Name = models.CharField(max_length=10)
    Last_Name = models.CharField(max_length=10)
    Age = models.IntegerField()
    Address = models.CharField(max_length=20)
    Contacts = models.IntegerField()
    Email = models.EmailField()
    username = models.CharField(max_length=10)
    password =models.CharField(max_length=10)



