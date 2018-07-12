from django.db import models

class employee(models.Model):
	eid = models.IntegerField(default=10, primary_key=True)
	username = models.CharField(max_length=40)
	fname = models.CharField(max_length=40)
	lname = models.CharField(max_length=40)
	password = models.CharField(max_length=255)
	salary = models.IntegerField(default=100)

