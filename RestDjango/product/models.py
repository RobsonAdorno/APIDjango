from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    amount = models.CharField(max_length=6)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category



