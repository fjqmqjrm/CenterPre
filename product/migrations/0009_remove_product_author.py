# Generated by Django 3.2.19 on 2023-07-11 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
    ]
