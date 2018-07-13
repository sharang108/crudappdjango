from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import employee
# Create your views here.

def login(request):
	t = get_template('login.html')
	html = t.render()
	return HttpResponse(html)

def home(request):
	t = get_template('index.html')
	html = t.render()
	return HttpResponse(html)	

def authenticate(request):
	if request.method == 'POST':
		x = request.body
	return HttpResponse(x)
