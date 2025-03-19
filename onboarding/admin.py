

# Register your models here.
from django.contrib import admin
from .models import Sale, Order, Product

admin.site.register(Sale)
admin.site.register(Order)
admin.site.register(Product)