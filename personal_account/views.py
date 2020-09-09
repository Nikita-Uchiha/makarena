from django.shortcuts import render
from .smsc_api import *
import random
from .forms import UserRegistrationForm, UserLoginForm, UserRegistrationForm2
from .models import CustomUser
from django.contrib.auth import authenticate, login
from orders.models import *
from django.http import HttpResponseRedirect


def regsms(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		print(form)
		if form.is_valid():
			print(1234)
			cd = form.cleaned_data
			user = authenticate(username=cd['phone'], password=cd['password'])
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/code/account')
				
			else:
				return HttpResponse('Invalid login')

	return render(request, 'mainapp/menu.html')



def code(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		print(user_form['phone'])
		x = random.randint(0000, 9999)
		code_sms = str(x)
		print(code_sms)
		# user2 = CustomUser.objects.get(id = 17)
		# user2.delete()
		
		smsc = SMSC()
		if user_form.is_valid():
			phones = user_form.cleaned_data.get("phone")
			print(type(phones))
			print(22)
			user = len(CustomUser.objects.filter(phone = user_form.cleaned_data.get("phone")))
			if user == 0:
				
				user1 = CustomUser.objects.create(phone = user_form.cleaned_data.get("phone"))
				user1.set_password(code_sms)
				# r = smsc.send_sms(phones, "Ваш код для регистрации на сайте:"+code_sms , sender="sms")
				user1.save()
				i = 1
				print(i)
				return render(request, 'mainapp/menu.html')
			else:
				
				user2 = CustomUser.objects.get(phone = user_form.cleaned_data.get("phone"))
				user2.set_password(code_sms)
				# r = smsc.send_sms(phones, "Ваш код для регистрации на сайте:"+code_sms , sender="sms")
				user2.save()
				i = 2
				print(i)
				return render(request, 'mainapp/menu.html')
		# else:
		# 	print(12345)

	return render(request, 'mainapp/menu.html')


def acc(request):
	print(request.user)
	plist = list()
	order = Order.objects.filter(phone = request.user.phone )
	for item in order:
		plist += OrderItem.objects.filter(order = item)

	form = UserRegistrationForm2(initial={'address_street': request.user.address_street,
										'email': request.user.email,  
										'address_house': request.user.address_house, 
										'address_entrance': request.user.address_entrance, 
										'address_apartment': request.user.address_apartment,
										'address_floor': request.user.address_floor,  
										'Birth_Date': request.user.Birth_Date, 
										'first_name': request.user.first_name })
	return render(request, 'personal_area.html', {'form':form, 'list' : order, 'plist':plist})


def update(request):
	if request.method == 'POST':
		form = UserRegistrationForm2(request.POST)
		if form.is_valid():
			user = CustomUser.objects.filter(phone = request.user).update(first_name = form.cleaned_data.get("first_name"),
																		Birth_Date = form.cleaned_data.get("Birth_Date"),
																		address_street = form.cleaned_data.get("address_street"),
																		email = form.cleaned_data.get("email"),
																		address_house = form.cleaned_data.get("address_house"),
																		address_entrance = form.cleaned_data.get("address_entrance"),
																		address_apartment = form.cleaned_data.get("address_apartment"),
																		address_floor = form.cleaned_data.get("address_floor"))

			return HttpResponseRedirect('/code/account')
		return HttpResponseRedirect('/code/account')


