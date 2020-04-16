from django.db import models

# Create your models here.
class Student(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	mobile = models.CharField(max_length=15)
	gender = models.CharField(max_length=40)
	email = models.CharField(max_length=40)
	collegename = models.CharField(max_length=40)
	age = models.IntegerField(blank=True, null=True)
	#age = models.CharField(max_length=40)
	regnum = models.CharField(max_length=40,unique=True)
	dob = models.CharField(max_length=40)
	university = models.CharField(max_length=40)
	username = models.CharField(max_length=40)
	password = models.CharField(max_length=40)

