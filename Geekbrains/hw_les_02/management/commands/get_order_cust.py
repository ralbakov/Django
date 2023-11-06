from django.core.management.base import BaseCommand, CommandParser
from hw_les_02.models import Customer, Order, Product

class Command (BaseCommand):
    help = "Get orders made by the сustomer."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=str, help='User ID')
    
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        сustomer = Customer.objects.filter(name=pk).first()
        if сustomer is not None:
            orders = Order.objects.filter(customer=сustomer)
            intro = f'all orders of {сustomer.name}\n'
            text = [order.date_ordered for order in orders]
            self.stdout.write(f'{intro}{text}')