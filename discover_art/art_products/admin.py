from django.contrib import admin

from discover_art.art_orders.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price')
    sortable_by = 'category'


admin.site.register(Product, ProductAdmin)