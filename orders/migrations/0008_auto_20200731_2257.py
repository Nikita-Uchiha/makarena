# Generated by Django 3.0.8 on 2020-07-31 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='number',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]