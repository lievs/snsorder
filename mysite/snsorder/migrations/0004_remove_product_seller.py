# Generated by Django 4.2.6 on 2023-11-18 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snsorder', '0003_product_seller_alter_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
    ]
