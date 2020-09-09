# Generated by Django 3.0.8 on 2020-08-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_account', '0002_customuser_address_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address_apartment',
            field=models.PositiveIntegerField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='address_entrance',
            field=models.PositiveIntegerField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='address_floor',
            field=models.PositiveIntegerField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='address_house',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]