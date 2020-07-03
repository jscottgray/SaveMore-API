from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from SaveOnFoods.models import Product, Price
from SaveOnFoods.serializers import ProductSerializer, PriceSerializer
import json


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


""" 
GET Requests
product_details: get product details, sku, name, etc
price_history: all price history for a product of single SKU
price_overview: current price, "on-sale" price, "average" price of single SKU
"""


@csrf_exempt
@require_GET
def product_details(request, sku):
    try:
        product = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    product_serializer = ProductSerializer(product)
    return JSONResponse(product_serializer.data)


@csrf_exempt
@require_GET
def price_history(request, sku):
    # TODO: implement this function, need to convert a QuerySet to JSON list of price objects?
    pass


@csrf_exempt
@require_GET
def price_overview(request, sku):
    prices = Price.objects.filter(sku=sku)
    prices_list = list(prices.all())
    number_of_prices = len(prices_list)
    sum_of_prices = 0
    lowest_price = 10000
    highest_price = 0
    for i in prices_list:
        sum_of_prices += i.price
        if i.price < lowest_price:
            lowest_price = i.price
        if i.price > highest_price:
            highest_price = i.price
    price_data = {}
    price_data['lowest price'] = lowest_price
    price_data['highest price'] = highest_price
    price_data['average price'] = sum_of_prices / number_of_prices
    json_data = json.dumps(price_data)
    return JSONResponse(json_data)


""" 
POST Requests
new_product: create a new Product
new_price: create a new Price
"""


@csrf_exempt
@require_POST
def new_product(request):
    product_data = JSONParser().parse(request)
    product_serializer = ProductSerializer(data=product_data)
    if product_serializer.is_valid():
        product_serializer.save()
        return JSONResponse(product_serializer.data,
                            status=status.HTTP_201_CREATED)
    return JSONResponse(product_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@require_POST
def new_price(request):
    price_data = JSONParser().parse(request)
    price_serializer = PriceSerializer(data=price_data)
    if price_serializer.is_valid():
        price_serializer.save()
        return JSONResponse(price_serializer.data,
                            status=status.HTTP_201_CREATED)
    return JSONResponse(price_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
