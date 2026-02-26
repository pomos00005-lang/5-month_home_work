from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)\
    
class Review(models.Model):
    text = models.CharField(max_length=10000)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    