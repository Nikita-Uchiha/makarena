# Generated by Django 3.0.8 on 2020-08-09 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20200809_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=0, default=None, max_digits=10, null=True),
        ),
    ]
