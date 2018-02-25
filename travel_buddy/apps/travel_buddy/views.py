# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from ..logreg.models import User
from models import *

# Create your views here.
def travels(request):
	context = {
		'user': User.objects.all(),
		'destination': Destination.objects.all(),
		'trip': Trips.objects.all(),
		'first_name': User.objects.get(id=request.session['user_id']).first_name,

	}
	return render(request, 'travels.html', context)

def add(request):
	print request.session['user_id']
	return render(request, 'add.html')

def addprocess(request):
	errors = Destination.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
			print "I did not work"
			print errors
		return redirect('/add/')
	if len(errors) == 0:
		# destination = models.OneToOneField(Destination, null=True, blank=True)
		currentuser = request.session['user_id']
		destination = Destination.objects.create()
		destination.destination = request.POST['destination']
		destination.desc = request.POST['desc']
		destination.datefrom = request.POST['datefrom']
		destination.dateto = request.POST['dateto']
		destination.user_id = User.objects.get(id=request.session['user_id'])
		destination.save()
		trip = Trips.objects.create()
		trip.destination_id = Destination.objects.last()
		trip.user_id = request.session['user_id']
		trip.save()
		return redirect('/travels/')

def join(request):
	return redirect('/travels/')

def destination(request, id):
	context = {
		'destination': Destination.objects.get(id=id),
	}
	return render(request, 'destination.html', context)