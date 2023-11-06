from django.urls import path
from .views import customer_prod

urlpatterns = [
    path('customer/<int:customer_id>/<int:order_delta>', customer_prod, name='customer_prod'),
]