from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='product', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places = 2, blank=True, null=True, default=None)
    weight = models.CharField(max_length=200, db_index=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True ,blank=True, null=True)
    pepper = models.BooleanField(default=False)
    bacon = models.BooleanField(default=False)
    mushrooms = models.BooleanField(default=False)
    cheese = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name



class Slider(models.Model):
    image = models.ImageField(upload_to='slider', blank=True)


    class Meta:
        verbose_name = 'Картинка для слайдера'
        verbose_name_plural = 'Картинки для слайдера'



class Akatsuki(models.Model):
    name = models.CharField(max_length = 40, db_index=True)
    description = models.CharField(max_length = 200, db_index=True)
    image = models.ImageField(upload_to='akatsuki', blank=True)

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'



class news(models.Model):
    name = models.CharField(max_length = 40, db_index=True)
    description = models.CharField(max_length = 200, db_index=True)
    image = models.ImageField(upload_to='news', blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Makarena_bar(models.Model):
    image = models.ImageField(upload_to='about_us', blank=True)


    class Meta:
        verbose_name = 'Картинка для старницы о нас'
        verbose_name_plural = 'Картинки для старницы о нас'




class file(models.Model):
    menu = models.FileField(upload_to = 'file', blank=True)
    class Meta:
        verbose_name = 'Файл меню'
        



