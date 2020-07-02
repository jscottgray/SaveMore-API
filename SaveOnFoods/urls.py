from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("product_list", views.product_list),
    path("product_detail/<int:SKU>", views.product_detail),
    # url(r'^product_detail/(?P<SK>[0-9]+)', views.product_detail),
    path("product", views.update_product)
]
