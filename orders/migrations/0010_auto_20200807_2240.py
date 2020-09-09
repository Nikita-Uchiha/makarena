# Generated by Django 3.0.8 on 2020-08-07 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_pay_met'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_apartment',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_entrance',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_floor',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
