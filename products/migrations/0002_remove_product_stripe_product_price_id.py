# Generated by Django 3.2.13 on 2023-04-11 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stripe_product_price_id',
        ),
    ]