# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def add(request):
	return render(request, 'add.html')

def users(request):
	context = {
		'users': Users.objects.all()
	}
	return render(request, 'usertable.html', context)

def show(request, id):
	context = {
		'user': Users.objects.get(id=id)
	}
	return render(request, 'user.html', context)



def edit(request, id):
	context = {
		'user': Users.objects.get(id=id)
	}
	return render(request, 'edit.html', context)

def edituser(request, id):
	errors = Users.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/edit/(?P<id>\d+)')

	else:
		user = Users.objects.get(id=id)
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()
		return redirect('/users/')

def adduser(request):
	errors = Users.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/add/')

	else:
		user = Users.objects.create()
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()
		return redirect('/add/')

def deleteuser(request, id):
	user = Users.objects.get(id=id)
	user.delete()
	return redirect('/users/')

def index(request):
	return redirect('/users/')