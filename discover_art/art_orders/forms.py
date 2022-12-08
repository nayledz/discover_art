from django.forms import models

from discover_art.art_orders.models import Order


class OrderForm(models.ModelForm):
    class Meta:
        model = Order
        fields = ('customer_first_name', 'customer_last_name', 'country', 'city', 'street', 'zip')
