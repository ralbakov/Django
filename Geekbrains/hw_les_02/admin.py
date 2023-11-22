from django.contrib import admin
from hw_les_02.models import Product, Customer, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date_add']
    ordering = ['price', 'quantity']
    list_filter = ['price']
    search_fields = ['name']
    search_help_text = 'Поиск по полю описание продукта (name)'
    actions = [reset_quantity]

    """Отдельный продукт."""
    # fields = ['name', 'description', 'price', 'quantity']
    readonly_fields = ['date_add', 'name']
    fieldsets = [
        (
            None,
            {'classes': ['wide'],
             'fields': ['date_add']},
        ),

        (
            'Подробности',
            {'classes': ['wide'],
             'description': 'Описание товара',
             'fields': ['name', 'description', 'image']},
        ),

        (
            'Цена и количество',
            {'fields': ['price', 'quantity']}
        ),
    ]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'telephone', 'reg_date']
    ordering = ['reg_date']
    list_filter = ['name']
    readonly_fields = ['email', 'address', 'reg_date', 'telephone']
    fieldsets = [
                    (None, {'classes': ['wide'],
                            'fields': ['name', 'address']}),

                    ('Данные пользователя', {'classes': ['wide'],
                                            'fields': ['telephone', 'email']}),

                    ('Прочая инфа', {'classes': ['collapse'],
                                    'fields': ['reg_date']})
    ]



admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)