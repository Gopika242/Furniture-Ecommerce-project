from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ContactDb(models.Model):
    FName=models.CharField(max_length=100,null=True,blank=True)
    LName=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Messages=models.TextField(max_length=100,null=True,blank=True)

class SignUpDb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    pass1=models.CharField(max_length=100,null=True,blank=True)
    re_pass=models.CharField(max_length=100, null=True, blank=True)

class CartDb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    ProductName=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    MRP=models.IntegerField(null=True,blank=True)
    Total=models.IntegerField(null=True,blank=True)

class OrderDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Place=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100, null=True, blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Address=models.CharField(max_length=100, null=True, blank=True)
    TotalAmount=models.IntegerField(null=True, blank=True)
    Messages=models.CharField(max_length=100,null=True,blank=True)

