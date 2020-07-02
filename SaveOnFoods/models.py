from django.db import models


class Product(models.Model):
    SKU = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    # in future will not have price field, using to test MVP
    price = models.FloatField()
