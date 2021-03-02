from django.contrib import admin

# Register your models here.
from lesson2.models import CarBrand, Car

admin.site.register(CarBrand)
admin.site.register(Car)

