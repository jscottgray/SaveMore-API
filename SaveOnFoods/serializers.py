from rest_framework import serializers
from SaveOnFoods.models import Product

# Serializers can be used to *both* serialize and deserialize data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["SKU", "name", "price"]
