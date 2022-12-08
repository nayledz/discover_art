# Generated by Django 4.1.3 on 2022-11-27 17:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('art_products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_complete', models.BooleanField(default=False)),
                ('ordered_date', models.DateTimeField()),
                ('customer_first_name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('customer_last_name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art_products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
