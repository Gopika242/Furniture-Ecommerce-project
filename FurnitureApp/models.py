from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    CategoryName=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(max_length=150,null=True,blank=True)
    CategoryImage=models.ImageField(upload_to='CategoryImages',null=True, blank=True)

class ProductDb(models.Model):
    Category=models.CharField(max_length=100, null=True, blank=True)
    ProductName=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    MRP=models.IntegerField(null=True, blank=True)
    PDescription=models.TextField(max_length=150,null=True,blank=True)
    Country=models.CharField(max_length=100,null=True,blank=True)
    Manufacturer=models.CharField(max_length=100,null=True,blank=True)
    ProductImage1=models.ImageField(upload_to='ProductImages',null=True, blank=True)
    ProductImage2=models.ImageField(upload_to='ProductImages',null=True, blank=True)
    ProductImage3=models.ImageField(upload_to='ProductImages',null=True, blank=True)