# Generated by Django 3.0.8 on 2020-08-08 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20200808_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Makarena_bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='about_us')),
            ],
            options={
                'verbose_name': 'Картинка для старницы о нас',
                'verbose_name_plural': 'Картинки для старницы о нас',
            },
        ),
    ]