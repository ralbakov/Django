from django.core.management.base import BaseCommand, CommandParser
from hw_les_02.models import Customer, Product
import random
import datetime

class Command (BaseCommand):
    help = "Fake data create customer and products"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('count', type=int, help='count fake customer and products')
    
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            customer = Customer(
                              name=f'Name_{i}', 
                              email=f'mail_{i}@mail.ru',
                              telephone=f"89{''.join([random.choice('0123456789') for _ in range(9)])}",
                              address=f'Address_{i}',
                              reg_date=datetime.datetime.now()
            )
            customer.save()
            products = Product(
                               name=f'NameProd_{i}', 
                               description=f'Description for NameProd_{i}', 
                               price=random.uniform(1, 1000),
                               quantity=random.randint(1, 100),
                               date_add=datetime.datetime.now()
                               )
            products.save()