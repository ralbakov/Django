from django.shortcuts import render, get_object_or_404
from hw_les_02.models import Customer, Order
from datetime import datetime, timedelta


def customer_prod(request, customer_id, order_delta):
    customer = get_object_or_404(Customer, pk=customer_id)
    delta_or = datetime.today()-timedelta(days=order_delta)
    orders = Order.objects.filter(customer=customer).filter(date_ordered__gt=delta_or)
    pr = []
    for order in orders:
        for product in order.products.all():
            if product not in pr:
                pr.append(product)
    context = {"title": f"Заказы {customer.name}",
               "customer": customer,
               "orders": orders,
               "products": pr,
               "delta_or": delta_or}
    return render(request, "hw_les_02/index.html", context)