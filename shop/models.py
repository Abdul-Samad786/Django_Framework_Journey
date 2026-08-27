from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name=models.CharField(max_length=50)

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    tags=models.ManyToManyField(Tag, through='Product_Tag', blank=True, related_name='products')
    sku = models.CharField(max_length=50,null=True)
class Product_Tag(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    tag=models.ForeignKey(Tag, on_delete=models.CASCADE)
    added_at=models.DateTimeField(auto_now_add=True)
    
class Listing(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    seller=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="listings_selling")
    buyer=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="listings_buying")
    created_at=models.DateTimeField(auto_now_add=True)

class PriceHistory(models.Model):
    Listing=models.ForeignKey(Listing, on_delete=models.CASCADE,related_name='price_histories'  )
    price=models.DecimalField(max_digits=10, decimal_places=2)
    timestamp=models.DateTimeField(auto_now_add=True)