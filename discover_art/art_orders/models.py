from django.core import validators
from django.db import models

from discover_art.art_auth.admin import UserModel
from discover_art.art_products.models import Product


class Order(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    order_complete = models.BooleanField(
        default=False,
    )
    ordered_date = models.DateTimeField(

    )
    customer_first_name = models.CharField(
        max_length=20,
        validators=(
            validators.MinLengthValidator(2),
        ),
        null=False,
        blank=False,
    )
    customer_last_name = models.CharField(
        max_length=20,
        validators=(
            validators.MinLengthValidator(2),
        ),
        null=False,
        blank=False,
    )
    country = models.CharField(
        max_length=20,
    )
    city = models.CharField(
        max_length=20,
    )
    street = models.CharField(
        max_length=50,
    )
    zip = models.CharField(
        max_length=20,
    )
