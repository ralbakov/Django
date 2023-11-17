import logging
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from hw_les_02.models import Customer, Order, Product
from datetime import datetime, timedelta
from .forms import ProductForm


logger = logging.getLogger(__name__)


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

def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            product = Product.objects.filter(name=name).first()
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            product.date_add = form.cleaned_data['date_add']
            image = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product.image = image
            product.save()
            logger.info(f'Обновили {product.name}')

    else:
        form = ProductForm()
    return render(request, 'hw_les_02/update_product_forms.html', {'form': form})