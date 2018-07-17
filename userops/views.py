from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from userops.models import employee
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from userops.forms import LoginForm
from django.views.decorators.csrf import csrf_exempt
import pdb #debugger
# Create your views here.

#pdb.set_trace()
@csrf_exempt
def login(request):
	response = None
	if request.method == 'GET':
		t = get_template('login.html')
		response = t.render()
	elif request.method == 'POST':
		uname = request.POST.get("username")
		passw = request.POST.get("password")
		ename = employee.authenticateEmployee(uname, passw) 
		if ename is not None:
			request.session['uname'] = ename
			response = render_to_response('user_home.html', {"uname": request.session['uname']})
	return HttpResponse(response)

def home(request):
	response = None
	if request.session['uname'] is not None:
		response = render_to_response('user_home.html', {"uname": request.session['uname']})
	else:
		t = get_template('index.html')
		response = t.render()
	return HttpResponse(response)	

# @cache_page(60 * 15)
# @csrf_protect
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
		modelResponse = employee.createEmployee(username, password, fname, lname, salary)
		if modelResponse == True: 
			response = redirect('/login')
		respose = redirect('/register')
	return response

def logout(request):
	if request.session['uname'] is not None:
		request.session['uname'] = None
	return redirect('/login')


# Ajax Request Handler
def userProfile(request):
	e = employee.getEmployee(request.session['uname'])
	data = { 
	'fname' : e.fname,
	'lname' : e.lname,
	'uname' : e.username,
	'salary': e.salary
	}
	return JsonResponse(data)


