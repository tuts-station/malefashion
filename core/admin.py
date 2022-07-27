from django.contrib import admin
from .models import *

# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    model = Slider
    list_display = ['name', 'description', ]

admin.site.register(Slider,SliderAdmin)
