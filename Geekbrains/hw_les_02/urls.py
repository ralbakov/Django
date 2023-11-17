from django.urls import path
from .views import customer_prod, product_form

urlpatterns = [
    path('customer/<int:customer_id>/<int:order_delta>', customer_prod, name='customer_prod'),
    path('product/', product_form, name='product_form'),
]