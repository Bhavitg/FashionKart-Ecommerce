# Generated by Django 3.0.6 on 2020-05-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='final_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=1000),
        ),
        migrations.AddField(
            model_name='order',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=1000),
        ),
        migrations.AddField(
            model_name='order',
            name='tax_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=1000),
        ),
    ]