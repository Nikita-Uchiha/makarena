# Generated by Django 3.0.8 on 2020-07-29 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200729_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
