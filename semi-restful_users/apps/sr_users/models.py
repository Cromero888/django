# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User_validator(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 3:
			errors['first_name'] = "First Name must be at least 3 characters"
		if len(postData['last_name']) < 3:
			errors['last_name'] = "Last Name must be at least 3 characters"
		if len(postData['email']) < 6:
			errors['email'] = "Email must be at least 6 characters"
		return errors

class Users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = User_validator()