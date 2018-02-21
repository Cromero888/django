# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course_validator(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['name']) < 3:
			errors['name'] = "Course Name must be at least 3 characters"
		return errors
class Courses(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = Course_validator()

