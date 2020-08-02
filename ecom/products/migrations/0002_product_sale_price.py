# Generated by Django 3.0.6 on 2020-05-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=29.9, max_digits=100, null=True),
        ),
    ]
