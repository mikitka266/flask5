from .models import Product
from django.contrib import admin


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'client')
    ordering = ('id', 'product_name')
    search_fields = ('product_name', 'price')
    list_filter = ('product_name', 'price')
    list_per_page = 10



admin.site.register(Product, OrderAdmin)


