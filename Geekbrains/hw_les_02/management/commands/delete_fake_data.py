from django.core.management.base import BaseCommand
from hw_les_02.models import Customer, Order, Product

class Command (BaseCommand):
    help = "Delete data create"
    
    def handle(self, *args, **kwargs):
        Customer.objects.all().delete()
        Order.objects.all().delete()
        Product.objects.all().delete()
        