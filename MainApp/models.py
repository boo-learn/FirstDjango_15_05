from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=32)  # красный
    # css_view = models.CharField(max_length=32) # red


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.TextField(max_length=5000, default="Стартовое описание")
    colors = models.ManyToManyField(to=Color)

    def __repr__(self):
        return f"Item: {self.name} | {self.brand}"
