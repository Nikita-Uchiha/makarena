from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
urlpatterns = [
	
    path("", views.code, name='code'),
  	path("check/", views.regsms, name='personal_account'),
  	path("account/", views.acc, name='account'),
  	path("update/", views.update, name='update'),
  	path("logout/", LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
app_name="per"