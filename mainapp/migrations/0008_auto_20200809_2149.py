# Generated by Django 3.0.8 on 2020-08-09 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20200809_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=0, default=100, max_digits=10),
        ),
    ]
