from django.db import models
from mainapp.models import Product

class Order(models.Model):
	session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
	name = models.CharField(max_length=100, blank=True, null=True, default=None)
	phone = models.CharField(max_length=100, blank=True, null=True, default=None)
	email = models.EmailField(blank=True, null=True, default=None)
	address_street = models.CharField(max_length=250, blank=True, null=True, default=None)
	address_house = models.CharField(max_length=250, blank=True, null=True, default=None)
	address_entrance = models.PositiveIntegerField(blank=True, null=True, default=None)
	address_apartment = models.PositiveIntegerField(blank=True, null=True, default=None)
	address_floor = models.PositiveIntegerField( blank=True, null=True, default=None)
	delivery = models.CharField(max_length=30, blank=True, null=True, default=None)
	pay_met = models.CharField(max_length=30, blank=True, null=True, default=None)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	total_price = models.DecimalField(max_digits=10, decimal_places = 2, blank=True, null=True, default=None)
	bonus_card = models.BooleanField(default=False)
	paid = models.BooleanField(default=False)
	comment = models.CharField(max_length=100, blank=True, null=True, default=None)
	class Meta:
		ordering = ('-created',)
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'



class OrderItem(models.Model):
	session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, blank=True, null=True, default=None)
	product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
	price = models.PositiveIntegerField()
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity