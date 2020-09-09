from django.shortcuts import render, redirect
from .models import *
from mainapp.models import Product 
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import send_mail
from django.conf import settings
from personal_account.forms import UserRegistrationForm, UserLoginForm


def checkout(request):
	session_key = request.session.session_key
	print(session_key)
	form = UserRegistrationForm()
	LoginForm = UserLoginForm()
	order = Order.objects.create(session_key = session_key)
	day = order.created.weekday()
	days = range(0,5)
	hour = order.created.hour
	print(order.created.time())
	if request.POST:
		print(request.POST)
		data = request.POST
		cart = Cart(request)	
		cart.clear()
		for name, value in data.items():
			if name.startswith("product_"):
				product_id = name.split("product_")[1]
				product = Product.objects.get(id=product_id)
				nmb = value
				OrderItem.objects.create(product=product, quantity = nmb, price = product.price, session_key = session_key )
				
	new_cart = OrderItem.objects.filter( session_key= session_key)		            
	
	return render(request, 'orders/step1.html', {'new_cart' : new_cart, 'form': UserRegistrationForm, 'LoginForm':LoginForm, 'order':order,
												'day':day, 'days': days, 'hour':hour})



def cart_remove(request, product_id):
	session_key = request.session.session_key
	product = OrderItem.objects.get(session_key = session_key, id = product_id)
	product.delete()
	return redirect('orders:orders')


def step2(request):
	form = UserRegistrationForm()
	LoginForm = UserLoginForm()
	session_key = request.session.session_key
	if request.user.is_authenticated:
		form2 = OrderCreateForm(initial={'address_street': request.user.address_street,
											  
											'address_house': request.user.address_house, 
											'address_entrance': request.user.address_entrance, 
											'address_apartment': request.user.address_apartment,
											'address_floor': request.user.address_floor,

											 })
	else:
		form2 = OrderCreateForm()
	if request.POST:
		print(request.POST)
		data = request.POST
		delivery = (data['radio'])
		total_price = data['content']
		order = Order.objects.filter(session_key = session_key).update(total_price = total_price, delivery = delivery)
		order = Order.objects.filter(session_key = session_key)[0]

		for name, value in data.items():
			if name.startswith("product_"):
				product_id = name.split("product_")[1]
				
				nmb = value
				OrderItem.objects.filter(session_key = session_key, id = product_id ).update(quantity= nmb, order = order)

	
	return render(request, 'orders/step2.html', {'form2' : form2, 'form': UserRegistrationForm, 'LoginForm':LoginForm})


def step3(request):
	form = UserRegistrationForm()
	LoginForm = UserLoginForm()
	session_key = request.session.session_key
	
	if request.POST:
		form = OrderCreateForm(request.POST)
		print(form['address_street'])
		if form.is_valid():
			order = Order.objects.filter(session_key = session_key).update(address_street = form.cleaned_data.get("address_street"),
																		address_house = form.cleaned_data.get("address_house"),
																		address_entrance = form.cleaned_data.get("address_entrance"),
																		address_apartment = form.cleaned_data.get("address_apartment"),
																		address_floor = form.cleaned_data.get("address_floor"),
																		bonus_card = form.cleaned_data.get("bonus_card"),
																		comment = form.cleaned_data.get("comment"))

	
	return render(request, 'orders/step3.html' , {'form': UserRegistrationForm, 'LoginForm':LoginForm})


def step4(request):
	form = UserRegistrationForm()
	LoginForm = UserLoginForm()
	session_key = request.session.session_key
	if request.POST:
		name =request.POST.get('name1')
		phone = request.POST.get('phone')
		mail =request.POST.get('mail')
		comment = request.POST.get('com')
		order = Order.objects.filter(session_key = session_key).update(name = name, phone = phone, email = mail, comment = comment )




	return render(request, 'orders/step4.html', {'form': UserRegistrationForm, 'LoginForm':LoginForm})




def step5(request):
	session_key = request.session.session_key
	if request.POST:
		data = request.POST
		pay_met = (data['radio'])
		orders = Order.objects.filter(session_key = session_key).update(pay_met = pay_met)
		order = Order.objects.filter(session_key = session_key)[0]
		item = OrderItem.objects.filter(session_key = session_key)

		mes = ""
		card = ""
		if order.bonus_card == True:
			card = "НУЖНО СДЕЛАТЬ БОНУСНУЮ КАРТУ"
		else : 
			card = ""
		for i in OrderItem.objects.filter(session_key = session_key):
			if i.product.category.name == "пицца":
				if i.product.pepper == True:
					pepper = " Перчик халапенье"
				else: 
					pepper = ""
				if i.product.bacon == True:
					bacon = " Бекон"
				else: 
					bacon = ""
				if i.product.mushrooms == True:
					mushrooms = " Грибы"
				else: 
					mushrooms = ""
				if i.product.cheese == True:
					cheese = " Сыр"
				else: 
					cheese = ""
				mes = mes + "Продукт  : " +  str(i.product.name) + pepper + bacon + mushrooms + cheese +"\n"\
							+ "кол-во  :" + str(i.quantity)+ "\n"\
							+ "Итого:  " + str(i.price) + "\n"
			else:

				mes = mes + "Продукт  : " +  str(i.product.name) + "\n"\
							+ "кол-во  :" + str(i.quantity)+ "\n"\
							+ "Итого:  " + str(i.price) + "\n"


		if pay_met == "Наличными" or pay_met == "Картой курьеру"  :
			subject = 'Карим лох'
			message = ""
			message = "Имя: "+ str(order.name) + "\n"\
							+ "Номер: " + str(order.phone) + "\n"\
							+ "Улица: " +  str(order.address_street) + "\n"\
							+ "Дом: " +  str(order.address_house) + "\n"\
							+ "Подъезд: " +  str(order.address_entrance) + "\n"\
							+ "Квартира: " +  str(order.address_apartment) + "\n"\
							+ "Этаж: " +  str(order.address_floor) + "\n"\
							+ "Доставка: " +  str(order.delivery) + "\n"\
							+ "Тип оплаты: " +  str(order.pay_met) + "\n"\
							+ "Комментарий к заказу: " +  str(order.comment) + "\n"\
							+ "Итого: " + str(order.total_price) + "\n"
			m3 = message + mes + card
			email_from = settings.EMAIL_HOST_USER
			recipient_list = ['karim90403@gmail.com',]
			send_mail( subject, m3, email_from, recipient_list )
			print(m3)
		
			return redirect('mainapp:mainapp')
		if pay_met == "Карой на сайте":
			return redirect('mainapp:mainapp')


	return redirect('mainapp:mainapp')

