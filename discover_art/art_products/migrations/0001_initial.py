# Generated by Django 4.1.3 on 2022-11-27 17:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('landscapes', 'Landscapes'), ('abstracts', 'Abstracts'), ('people_and_portraits', 'People and Portraits'), ('florals_and_plants', 'Florals and Plants'), ('still_life', 'Still Life'), ('animals', 'Animals'), ('architecture_and_cities', 'Architecture and Cities')], max_length=30)),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('product_image', models.ImageField(upload_to='products')),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
