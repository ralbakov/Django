from django import forms
import datetime
from hw_les_02.models import Product


class ProductForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Product.objects.all(),label='Продукт')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    price = forms.DecimalField(max_digits=8, decimal_places=2, label='Цена')
    quantity = forms.DecimalField(max_digits=8, decimal_places=3, label='Количество')
    date_add = forms.DateTimeField(initial=datetime.date.today, localize=True,
                                   widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}), label='Дата добавления')
    image = forms.ImageField()