# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User

# Create your models here.
class Friend(models.Model):
	friend1 = models.ForeignKey(User, related_name='friender')
	friend2 = models.ForeignKey(User, related_name='friendee')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
# 	objects = something_validator()

# class Something_validator(models.Manager):
# 	def basic_validator(self, postData):