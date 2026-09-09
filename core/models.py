from os import name
from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    quantity = models.IntegerField()

    def __str__(self):
        return self.name