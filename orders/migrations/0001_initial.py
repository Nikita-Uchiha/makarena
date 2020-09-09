# Generated by Django 3.0.8 on 2020-07-28 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0002_auto_20200714_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('address_street', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('address_house', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('address_entrance', models.PositiveIntegerField(blank=True, default=None, max_length=250, null=True)),
                ('address_apartment', models.PositiveIntegerField(blank=True, default=None, max_length=250, null=True)),
                ('address_floor', models.PositiveIntegerField(blank=True, default=None, max_length=250, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='mainapp.Product')),
            ],
        ),
    ]
