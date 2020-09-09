from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from cart.cart import Cart
from cart.forms import CartAddProductForm
from .models import Product, Slider, Akatsuki, news, Makarena_bar, file
from personal_account.forms import UserRegistrationForm, UserLoginForm
from personal_account.models import CustomUser
from django.conf import settings
from django.core.mail import send_mail


def mainapp(request):
	slider = Slider.objects.all()
	business_lunch = Product.objects.filter(category__name = "бизнес_ланч")
	hot_dishes = Product.objects.filter(category__name = "горячие_закуски") 
	ramen = Product.objects.filter(category__name = "супы")
	itachi = Product.objects.filter(category__name = "гриль_меню")
	rolls = Product.objects.filter(category__name = "ролы")
	pasta = Product.objects.filter(category__name = "паста")
	salad = Product.objects.filter(category__name = "салаты")
	snack = Product.objects.filter(category__name = "закуски")
	beer_snack = Product.objects.filter(category__name = "закуски_к_пиву")
	garnish = Product.objects.filter(category__name = "гарниры")
	sause = Product.objects.filter(category__name = "соусы")
	dessert = Product.objects.filter(category__name = "дессерты")
	cocktail = Product.objects.filter(category__name = "коктейли")
	milk = Product.objects.filter(category__name = "молочные_коктейли_смузи_и_ласси")
	fresh_juise = Product.objects.filter(category__name = "свежавыжатые_соки")
	limo = Product.objects.filter(category__name = "лимонады", weight = 350)
	limo2 = Product.objects.filter(category__name = "лимонады", weight = 1000)
	cold_drink = Product.objects.filter(category__name = "прохладительные_напитки")
	hot_drink = Product.objects.filter(category__name = "горячие_напитки")
	tea = Product.objects.filter(category__name = "чайная_карта")
	special_tea = Product.objects.filter(category__name = "авторскипе_чаи")
	coffee = Product.objects.filter(category__name = "кофейная_карта")
	cold_coffee = Product.objects.filter(category__name = "холодный_кофе")
	pizza = Product.objects.filter(category__name = "пицца" , pepper = False, bacon= False, mushrooms = False, cheese = False )
	cart = Cart(request)
	cart_product_form = CartAddProductForm()
	form = UserRegistrationForm()
	LoginForm = UserLoginForm()
	if request.user.is_authenticated:
		print(request.user.first_name)
	return render(request , 'mainapp/menu.html', {"business_lunch": business_lunch,
											"hot_dishes" : hot_dishes, 
											"ramen" : ramen,
											"itachi" : itachi,
											"rolls" : rolls,
											"salad" : salad,
											"snack" : snack,
											"beer_snack" : beer_snack,
											"garnish" : garnish,
											"sause" : sause,
											"dessert" : dessert,
											"cocktail" : cocktail,
											"milk" : milk,
											"fresh_juise" : fresh_juise,
											"limo" : limo,
											"limo2":limo2,
											"cold_drink" : cold_drink,
											"hot_drink" : hot_drink,
											"tea" :tea,
											"special_tea" : special_tea,
											"coffee" : coffee,
											"cold_coffee" : cold_coffee,
											"pasta" : pasta,
											'cart': cart,
											'pizza':pizza,
											'cart_product_form': cart_product_form,
											'form': UserRegistrationForm,
											'LoginForm':LoginForm,
											'slider': slider
											
											 })

def get_Akatsuki(request):
	akatsuki = Akatsuki.objects.all()
	cart = Cart(request)
	form = UserRegistrationForm()
	LoginForm = UserLoginForm()
	return render(request, "mainapp/akcii.html", {'cart': cart,'form': UserRegistrationForm, 'LoginForm':LoginForm, 'akatsuki': akatsuki })

def get_news(request):
	news1 = news.objects.all()
	cart = Cart(request)
	form = UserRegistrationForm()
	LoginForm = UserLoginForm()
	return render(request, "mainapp/news.html", {'cart': cart,'form': UserRegistrationForm, 'LoginForm':LoginForm, 'news': news1 })


def vacancies(request):
	cart = Cart(request)
	form = UserRegistrationForm()
	LoginForm = UserLoginForm()
	return render(request, "mainapp/vacansies.html", {'cart': cart,'form': UserRegistrationForm, 'LoginForm':LoginForm})

def delivery(request):
	cart = Cart(request)
	form = UserRegistrationForm()
	LoginForm = UserLoginForm()
	return render(request, "mainapp/delivery.html", {'cart': cart,'form': UserRegistrationForm, 'LoginForm':LoginForm})

def payment(request):
	cart = Cart(request)
	form = UserRegistrationForm()
	LoginForm = UserLoginForm()
	return render(request, "mainapp/payment.html", {'cart': cart,'form': UserRegistrationForm, 'LoginForm':LoginForm })

def about_us(request):
	slider = Makarena_bar.objects.all()
	menu = file.objects.get(id = 1)
	cart = Cart(request)
	form = UserRegistrationForm()
	LoginForm = UserLoginForm()
	return render(request, "mainapp/macarena.html", {'cart': cart,'form': UserRegistrationForm, 'LoginForm':LoginForm, "slider" :slider,
													'menu':menu})


def reservation(request):
	if request.method == 'POST':
		subject = 'Карим лох'
		phone = request.POST.get('phone')
		message = "Позвонить по вопросу брони:" + str(phone)
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ['karim90403@gmail.com',]
		send_mail( subject, message, email_from, recipient_list )
		print(message)
		return redirect('mainapp:mainapp')




@require_POST
def detail(request, i_id):
	product = get_object_or_404(Product, id=id,)
	cart_product_form = CartAddProductForm()
	return render(request, 'mainapp/okno.html', {'product': product, 'cart_product_form': cart_product_form})


def cart_add(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id = product_id)
	form = CartAddProductForm(request.POST)
	if request.method == 'POST':
		if request.POST.get('num', False):
			m = int(request.POST['num'])
			if m == 0:
				return redirect('mainapp:mainapp')
			else:
				cart.add(product=product, quantity=m, update_quantity=form)
	return redirect('mainapp:mainapp')

def cart_add2(request, product_id):
	print (request.POST)
	cart = Cart(request)
	product = get_object_or_404(Product, id = product_id)
	form = CartAddProductForm(request.POST)
	if request.method == 'POST':
		if request.POST.get('num', False):
			m = int(request.POST['num'])
			if m == 0:
				return redirect('mainapp:mainapp')
			elif "radio" in request.POST:
				if '1' in request.POST.getlist('radio'):
					pepper = True
				else :
					pepper = False
				if '2' in request.POST.getlist('radio'):
					bacon = True
				else :
					bacon = False
				if '3' in request.POST.getlist('radio'):
					mushrooms = True
				else :
					mushrooms = False
				if '3' in request.POST.getlist('radio'):
					cheese = True
				else :
					cheese = False
				product2 = get_object_or_404(Product, name = product.name , pepper = pepper, bacon= bacon, mushrooms = mushrooms, cheese= cheese)
				cart.add(product=product2, quantity=m, update_quantity=form)

			else:
				cart.add(product=product, quantity=m, update_quantity=form)
	return redirect('mainapp:mainapp')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('mainapp:mainapp')



