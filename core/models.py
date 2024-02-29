from django.utils import timezone
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    codprod = models.IntegerField()
    nameprod = models.CharField(max_length=255)
    priceprod = models.DecimalField(max_digits=5, decimal_places=2)
    desprod = models.TextField()
    avprod = models.IntegerField()
    catprod = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.nameprod
    
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    date = models.DateTimeField()
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)   

    def __str__(self):
        return self.client.name
