# Generated by Django 3.0.8 on 2020-08-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_account', '0004_customuser_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Birth_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
