# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
	context = {
		'courses': Courses.objects.all()
	}
	return render(request, 'courses.html', context)

def remove(request, id):
	context = {
		'course': Courses.objects.get(id=id)
	}
	return render(request, 'delete.html', context)

def deletecourse(request, id):
	course = Courses.objects.get(id=id)
	course.delete()
	return redirect('/')

def addcourse(request):
	errors = Courses.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		course = Courses.objects.create()
		course.name = request.POST['name']
		course.desc = request.POST['description']
		course.save()
		return redirect('/')