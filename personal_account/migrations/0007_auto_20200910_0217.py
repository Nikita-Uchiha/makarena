# Generated by Django 3.1.1 on 2020-09-10 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_account', '0006_auto_20200807_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]