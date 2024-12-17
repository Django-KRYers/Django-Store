from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    

class Cart(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="ProductCart", related_name='carts')

    # def total_sum_price(self, products):


