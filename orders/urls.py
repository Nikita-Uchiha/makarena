from django.urls import path
from . import views

urlpatterns = [
	
    path("", views.checkout, name='orders'),
    path("remove/<int:product_id>", views.cart_remove, name='cart_remove'),
    path("step2", views.step2, name='step2'),
    path("step2/step3", views.step3, name='step3'),
    path("step2/step3/step4", views.step4, name='step4'),
    path("step2/step3/step4/step5", views.step5, name='step5'),
]
app_name="orders"