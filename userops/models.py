from django.db import models

class employee(models.Model):
	eid = models.AutoField(default=10, primary_key=True) #auto increment autoField
	username = models.CharField(max_length=40)
	fname = models.CharField(max_length=40)
	lname = models.CharField(max_length=40)
	password = models.CharField(max_length=255)
	salary = models.IntegerField(default=100)


	def createEmployee(uname, fname, lname, passw, salary):
		response = False
		e = employee(username=uname, fname=fname, lname=lname, password=passw, salary=salary)
		e.save()
		e = employee.objects.get(username=uname)
		if e.username == uname: 
			response = True
		return response

	def authenticateEmployee(uname, passw):
		response = None
		e = employee.objects.get(username=uname)
		if passw == e.password:
			response = e.username
		return response

	def getEmployee(uname):
		return employee.objects.get(username=uname)