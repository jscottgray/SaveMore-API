from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # GET Requests
    path("product_details/<int:sku>", views.product_details),
    path("price_history/<int:sku>", views.price_history),
    path("price_overview/<int:sku>", views.price_overview),
    # POST Requests
    path("new_product", views.new_product),
    path("new_price", views.new_price),
]
