from rest_framework import serializers
from SaveOnFoods.models import Product, Price

# Serializers can be used to *both* serialize and deserialize data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["sku", "name", "description", "size", "department"]


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ["sku", "price", "multibuy", "sales_description"]
