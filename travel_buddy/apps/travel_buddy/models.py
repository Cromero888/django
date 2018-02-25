# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User

# Create your models here.
class Destination_validator(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['destination']) < 3:
			errors['destination'] = "Please write a Destination"
		if len(postData['desc']) < 4:
			errors['desc'] = "Please write at description"
		# if postData['datefrom'] == None:
		# 	errors['datefrom'] = "Please enter a start date"
		# if postData['dateto'] == None:
		# 	errors['dateto'] = "please enter an end date"
		return errors

class Destination(models.Model):
	destination = models.CharField(max_length=255)
	desc = models.TextField()
	datefrom = models.CharField(max_length=255)
	dateto = models.CharField(max_length=255)
	user = models.ForeignKey(User, related_name='Destination')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# trips = models.ManytoManyField(User, related_name='dest')
	objects = Destination_validator()

class Trips(models.Model):
	destination = models.ForeignKey(Destination, related_name='users')
	user = models.ForeignKey(User, related_name='destinations')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)