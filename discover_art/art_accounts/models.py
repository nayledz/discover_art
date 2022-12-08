from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from discover_art.core.validators import validate_only_letters

UserModel = get_user_model()


class Account(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30


    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        ),
        verbose_name='First Name',
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        ),
        verbose_name='Last Name',
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(18),
        ),
        null=True,
        blank=True,
    )
    profile_picture = models.ImageField(
        upload_to='accounts',
        default='staticfiles/images/default-profile.png',
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'