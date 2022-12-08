from django.contrib import admin

from discover_art.art_orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'customer_first_name', 'customer_last_name')
    sortable_by = 'ordered_date'


admin.site.register(Order, OrderAdmin)
