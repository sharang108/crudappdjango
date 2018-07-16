from django.db import models

class employee(models.Model):
	eid = models.AutoField(default=10, primary_key=True) #auto increment autoField
	username = models.CharField(max_length=40)
	fname = models.CharField(max_length=40)
	lname = models.CharField(max_length=40)
	password = models.CharField(max_length=255)
	salary = models.IntegerField(default=100)


	def createEmployee(uname, fname, lname, passw, salary):
		e = employee(username=uname, fname=fname, lname=lname, password=passw, salary=salary)
		e.save()

	def authenticateEmployee(uname, passw):
		response = False
		e = employee.objects.get(username=uname)
		if passw == e.password:
			response = True
		return response