from enum import Enum

from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from discover_art.core.model_mixins import ChoicesEnumMixin

UserModel = get_user_model()


class Category(ChoicesEnumMixin, Enum):
    landscapes = 'Landscapes'
    abstracts = 'Abstracts'
    people_and_portraits = 'People and Portraits'
    florals_and_plants = 'Florals and Plants'
    still_life = 'Still Life'
    animals = 'Animals'
    architecture_and_cities = 'Architecture and Cities'


class Product(models.Model):
    category = models.CharField(
        max_length=30,
        choices=Category.choices(),
        null=False,
        blank=False,
    )
    name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
        ),
        null=False,
        blank=False,
    )
    price = models.FloatField(
        validators=(
            validators.MinValueValidator(0),
        ),
        null=False,
        blank=False,
    )
    product_image = models.ImageField(
        upload_to='products',
        null=False,
        blank=False,
    )
    description = models.TextField(
        max_length=300,
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    size = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    used_materials = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.quantity} of {self.name}"

    @property
    def total_item_price(self):
        return self.quantity * self.price


class Meta:
    verbose_name_plural = "products"
