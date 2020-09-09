from django.urls import path
from cart import views

urlpatterns = [
	
    path("", views.cart, name='cart'),
    path("remove/<int:product_id>", views.cart_remove, name='cart_remove'),
     



]
app_name="cart"