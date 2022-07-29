from django.db import models

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

# class Brand(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    category = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    # brand = models.OneToOneField(Brand,on_delete=models.CASCADE)
    label = models.CharField(choices=LABEL, max_length=150)
    name = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to='productImages/',null=True,blank=True)
    quantity = models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False,blank=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending = models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.name

