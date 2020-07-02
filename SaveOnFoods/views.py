from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from SaveOnFoods.models import Product
from SaveOnFoods.serializers import ProductSerializer
import json


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return JSONResponse(products_serializer.data)

    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if not product_serializer.is_valid():
            return JSONResponse(product_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        product_serializer.save()
        return JSONResponse(product_serializer.data,
                            status=status.HTTP_201_CREATED)


@csrf_exempt
def product_detail(request, SKU):
    if request.method != 'GET':
        return HttpResponse(status.HTTP_404_METHOD_NOT_ALLOWED)
    try:
        product = Product.objects.get(SKU=SKU)
    except Product.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    product_serializer = ProductSerializer(product)
    return JSONResponse(product_serializer.data)


@csrf_exempt
def update_product(request):
    if request.method not in ['PUT', 'DELETE']:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    product_data = JSONParser().parse(request)
    new_product = False
    try:
        product = Product.objects.get(SKU=product_data.SKU)
    except Product.DoesNotExist:
        # create a new product
        # in theory, you could delete a new product, but would have no effect overall
        new_product = True
        product = Product(SKU=product_data.SKU,
                          name=product_data.name,
                          price=product_data.price)
    if request.method == 'PUT':
        # create or update the product
        # add the SKU into the product data
        product_serializer = ProductSerializer(product, data=product_data)
        if new_product:
            response = status.HTTP_201_CREATED
        else:
            response = status.HTTP_200_OK
        if product_serializer.is_valid():
            product_serializer.save()
            return JSONResponse(product_serializer.data, status=response)
        return JSONResponse(product_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
