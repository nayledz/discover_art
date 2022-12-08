from django.core import validators
from django.db import models

from discover_art.core.validators import validate_only_letters


class ArtContact(models.Model):

    email = models.EmailField(
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            validate_only_letters,
        ),
        verbose_name='First Name',
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            validate_only_letters,
        ),
        verbose_name='Last Name',
        null=True,
        blank=True,
    )

    message = models.TextField(
        max_length=500,
        validators=(validators.MinLengthValidator(10),
                    ),
    )
    date_received = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Contact Us'
