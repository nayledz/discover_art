# Generated by Django 4.1.3 on 2022-11-27 17:15

import discover_art.core.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('art_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), discover_art.core.validators.validate_only_letters], verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), discover_art.core.validators.validate_only_letters], verbose_name='Last Name')),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(18)])),
                ('profile_picture', models.ImageField(blank=True, default='staticfiles/images/default-profile.png', null=True, upload_to='accounts', verbose_name='Profile Picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
