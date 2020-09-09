from django.urls import path
from . import views

urlpatterns = [
	path("", views.mainapp, name = 'mainapp' ),
    path("add/<int:product_id>", views.cart_add, name='cart_add'),
    path("add2/<int:product_id>", views.cart_add2, name='cart_add2'),
    path("remove/<int:product_id>", views.cart_remove, name='cart_remove'),
    path("promotions", views.get_Akatsuki, name='Akatsuki'),
    path("news", views.get_news, name='news'),
    path("vacancies", views.vacancies, name='vacancies'),
    path("delivery", views.delivery, name='delivery'),
    path("payment", views.payment, name='payment'),
    path("about_us", views.about_us, name='about_us'),
    path("reservation", views.reservation, name='reservation')

]
app_name="mainapp"

