from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from userops.models import employee
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from userops.forms import LoginForm
from django.views.decorators.csrf import csrf_exempt
import pdb #debugger
# Create your views here.

#pdb.set_trace()
def login(request):
	t = get_template('login.html')
	html = t.render()
	return HttpResponse(html)

def home(request):
	t = get_template('index.html')
	html = t.render()
	return HttpResponse(html)	

# @cache_page(60 * 15)
# @csrf_protect
@csrf_exempt
def authenticate(request):
	response = None
	if request.method == 'POST':
		uname = request.POST.get("username")
		passw = request.POST.get("password")
		if employee.authenticateEmployee(uname, passw) == True:
			response = get_template('home.html').render()
	return HttpResponse(response)

@csrf_exempt
def register(request):
	if request.method == 'GET':
		response = None
		response = get_template('register.html').render()
		response = HttpResponse(response)
	elif request.method == 'POST':
		username = request.POST.get("username")
		password = request.POST.get("password")
		fname = request.POST.get("fname")
		lname = request.POST.get("lname")
		salary = request.POST.get("salary")
		employee.createEmployee(username, password, fname, lname, salary)
		response = redirect('/login')
	return response