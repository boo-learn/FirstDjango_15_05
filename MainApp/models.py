from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.TextField(max_length=5000, default="Стартовое описание")

    def __repr__(self):
        return f"Item: {self.name} | {self.brand}"
