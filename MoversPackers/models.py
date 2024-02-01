from statistics import mode
from tkinter import CASCADE
from tokenize import tabsize
from django.db import models
from django.contrib.auth.models import User
from django.forms import DateField

# Create your models here.

class SiteUser(models.Model):
    name = models.CharField(max_length= 100,null=True)
    email = models.EmailField(max_length=100, null=True)
    mobile = models.CharField(max_length=15,null=True)
    location = models.CharField(max_length=200,null=True)
    shiftingloc = models.CharField(max_length=200,null=True)
    shiftingdate = models.DateField(null= True)
    briefitems = models.CharField(max_length=100,null=True)
    items = models.CharField(max_length=5000,null=True)
    requestdate = models.DateField(null=True)
    remark = models.CharField(max_length=500,null=True)
    status = models.CharField(max_length=30,null=True)
    updatationdate = models.DateField(null=True)
    def __str__(self):
        return self.name 


class Services(models.Model):
    title = models.CharField(max_length=100,null=True)
    discription = models.CharField(max_length=5000,null=True)
    image = models.FileField(null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=15,null=True)
    emailid = models.EmailField(max_length=100,null=True)
    subject = models.CharField(max_length=100,null=True)
    message = models.CharField(max_length=100,null=True)
    mdate = models.DateField(null=True) 
    isread = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.name

