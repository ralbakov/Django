from django.shortcuts import render, get_object_or_404
from hw_les_02.models import Customer, Order
from datetime import datetime, timedelta


def customer_prod(request, customer_id, order_delta):
    customer = get_object_or_404(Customer, pk=customer_id)
    delta_or = datetime.today()-timedelta(days=order_delta) # задаем с какого периода (даты) нам получить данные
    orders = Order.objects.filter(customer=customer).filter(date_ordered__gt=delta_or) # первый фильтр получает пользователя, второй - спецификатор позволяет найти объекты начиная с периода заданного выше 
    temp_prod = [] # по заданию нам нужно чтобы "Товары в списке не должны повторятся" поэтому применяю блок с 10 по 14 строку
    for order in orders:
        for product in order.products.all():
            if product not in temp_prod:
                temp_prod.append(product)
    context = {"title": f"Заказы {customer.name}",
               "customer": customer,
               "orders": orders,
               "products": temp_prod,
               "delta_or": delta_or}
    return render(request, "hw_les_02/index.html", context)