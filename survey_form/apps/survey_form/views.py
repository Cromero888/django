# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	return render(request, "index.html")

def process(request):
	count=0
	if request.method =="POST":
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
	return redirect("/result/")
	

def result(request):
	count=0
	context={
		'count': count,
	}
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 1
	return render(request, 'result.html', context)
