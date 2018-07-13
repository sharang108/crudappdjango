from django.urls import path
from . import views
from django.template.loader import get_template
from django.http import HttpResponse

urlpatterns = [
	path('login', views.login, name="login"),
	path('', views.home, name="home"),
	path('authenticate', views.authenticate, name="home")
	#path('/register', views.register)
]