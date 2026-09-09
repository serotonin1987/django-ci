from os import name
from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Note(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def get_created_at(self):
        return "2024-01-01"