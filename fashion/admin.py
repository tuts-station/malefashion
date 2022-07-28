from django.contrib import admin
from .models import *

# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    model = Slider
    list_display = ['name', 'description', ]

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['category', 'name','label', 'product_image', 'quantity', 'original_price', 'description', 'status', 'trending', ]

class CatagoryAdmin(admin.ModelAdmin):
    model = Catagory
    list_display = ['name','description','status','created_at', ]

admin.site.register(Slider,SliderAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Catagory,CatagoryAdmin)
