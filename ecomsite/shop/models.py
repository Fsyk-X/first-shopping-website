from django.db import models

# Create your models here.

class Products(models.Model):

    def __str__(self):
        return self.prodTitle
    
    prodTitle = models.CharField(max_length=100)
    prodPrice = models.FloatField()
    prodDiscount = models.FloatField()
    prodCategory = models.CharField(max_length=50)
    prodDescription = models.TextField()
    prodImage = models.CharField(max_length=300)

class Order(models.Model):

    def __str__(self):
        return self.custName
    
    items = models.CharField(max_length=1000)
    custName = models.CharField(max_length=100)
    custEmail = models.CharField(max_length=100)
    custAddress = models.CharField(max_length=200)
    custCity = models.CharField(max_length=50)
    custState = models.CharField(max_length=50)
    custZipcode = models.CharField(max_length=20)
    total = models.CharField(max_length=200)