from django.core.management.base import BaseCommand, CommandParser
from hw_les_02.models import Customer, Order, Product
import random
import datetime

class Command (BaseCommand):
    help = "Delete data create"
    
    def handle(self, *args, **kwargs):
        Customer.objects.all().delete()
        Order.objects.all().delete()
        Product.objects.all().delete()
        