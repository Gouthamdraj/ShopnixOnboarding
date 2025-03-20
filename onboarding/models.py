from django.db import models

# Create your models here.
from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='themes/')

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PricingPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed
    def __str__(self):
        return self.name


class Sale(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale on {self.date}: Rs. {self.amount}"

class Order(models.Model):
    status = models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_date = models.DateField()

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    sales_count = models.IntegerField()

    def __str__(self):
        return self.name