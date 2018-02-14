# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import datetime

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	request.session
	if "total" not in request.session:
		request.session['total'] = 0
	return render(request, "index.html")

def find(request):
	if request.method == "POST":
		if request.POST['thing'] == "farm":
			request.session['job'] = request.POST['thing']
			request.session['job'] = int(random.randrange(10, 21))
			
		if request.POST['thing'] == 'cave':
			request.session['job'] = request.POST['thing']
			request.session['job'] = int(random.randrange(5, 11))
			
		if request.POST['thing'] == 'house':
			request.session['job'] = request.POST['thing']
			request.session['job'] = int(random.randrange(2, 6))

		if request.POST['thing'] == 'casino':
			request.session['job'] = request.POST['thing']
			request.session['job'] = int(random.randrange(-50, 51))
			
	request.session['total'] += request.session['job']
	
	try:
		request.session['log']
	except:
		request.session['log'] = []
	if request.session['job'] >= 0:
		request.session['log'].append({
				'thing': request.POST['thing'],
				'job': request.session['job'],
				'now': datetime.datetime.now().strftime('%H:%m, %d %B, %Y'),
				'color': 'color:green;',
				'str1': 'You went to the',
				'str2': 'and earned',
				'str3': 'gold pieces at'
			})
	if request.session['job'] < 0:
		request.session['log'].append({
				'thing': request.POST['thing'],
				'job': request.session['job'],
				'now': datetime.datetime.now().strftime('%H:%m, %d %B, %Y'),
				'color': 'color:red;',
				'str1': 'You went to the',
				'str2': 'and lost (ouch)',
				'str3': 'gold pieces at'
			})
	return redirect('/')

def clear(request):
	request.session.flush()
	return redirect('/')