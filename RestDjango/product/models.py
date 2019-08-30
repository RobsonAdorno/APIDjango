from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    amount = models.CharField(max_length=6)
    category = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_length=3, decimal_places=2)

    def __init__(self, name, amount, category, unit_price):
        self.name = name
        self.amount = amount
        self.category = category
        self.unit_price = unit_price

    def __str__(self):
        return self.name



