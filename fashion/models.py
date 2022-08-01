from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Slider(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Catagory(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.name

LABEL = (
    ('New', 'New'),
    ('Best Seller', 'Best Seller'),
    ('Sale', 'Sale'),
)

class Brand(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,default=1)
    label = models.CharField(choices=LABEL, max_length=150)
    name = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to='productImages/',null=True,blank=True)
    quantity = models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False,blank=False)
    discounted_price = models.FloatField(null=False,blank=False,default='100.00')
    desc = models.TextField(max_length=500,null=False,blank=False)
    long_desc = models.TextField(null=False,blank=False,default='')
    status = models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending = models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
  
    # Below Property will be used by checkout.html page to show total cost in order summary
    @property
    def total_cost(self):
        return self.quantity * self.product.original_price

class FavouriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)