# Generated by Django 4.1.3 on 2022-12-01 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artcontact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]