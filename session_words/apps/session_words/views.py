# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
import datetime

# Create your views here.
def index(request):
	request.session
	return render(request, 'words.html')

def process(request):
	if request.method == "POST":
		request.session['word'] = request.POST['word']
		request.session['colorpick'] = request.POST['colorpick']
		request.session['now'] = datetime.datetime.now().strftime('%H:%m, %d %B, %Y')
		
		
	try:
		request.session['stuff']
	except:
		request.session['stuff']=[]
	request.session['stuff'].append(
		{'color':request.POST['colorpick'], 
		'word': request.POST['word'],
		'now': datetime.datetime.now().strftime('%H:%m, %d %B, %Y'),
		'bold': 'font-weight: 400;'})
	if 'bold' in request.POST:
		request.session['stuff'][len(request.session['stuff'])-1]['bold'] = "font-weight: 700;"
	return redirect('/')

def clear(request):
	request.session.flush()
	return redirect('/')