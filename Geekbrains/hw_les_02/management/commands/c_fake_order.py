from django.core.management.base import BaseCommand, CommandParser
from hw_les_02.models import Customer, Order, Product
import random
import datetime

class Command (BaseCommand):
    help = "Fake data create order"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('count', type=int, help='Count fake orders')
    
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            order_1 = Order.objects.create()
            order_1.save()
            order_1.customer = Customer.objects.get(name=f'Name_{random.randint(1, 10)}')
            p1=Product.objects.get(name=f'NameProd_{random.randint(1, 10)}')
            p2=Product.objects.get(name=f'NameProd_{random.randint(1, 10)}')
            order_1.products.add(p1, p2)
            total_price = p1.price * p1.quantity + p2.price * p2.quantity
            order_1.total_price = total_price
            order_1.date_ordered = datetime.datetime.now()
            order_1.save()
