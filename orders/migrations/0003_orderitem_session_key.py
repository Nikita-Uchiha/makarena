# Generated by Django 3.0.8 on 2020-07-29 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200728_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]