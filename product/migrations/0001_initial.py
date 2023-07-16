# Generated by Django 3.2.20 on 2023-07-08 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=256, verbose_name='상품명')),
                ('price', models.IntegerField(verbose_name='상품가격')),
                ('description', models.TextField(verbose_name='상품 상세설명')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
            ],
        ),
    ]
