# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def start(request):
	return redirect('/amadon/')

def reset(request):
	request.session.flush()
	return redirect('/amadon/')

def index(request):
	if "totalamount" not in request.session:
		request.session['totalamount'] = 0
	if "totalquantity" not in request.session:
		request.session['totalquantity'] = 0
	return render(request, 'amadon.html')

def buy(request):


	request.session['quantity'] = request.POST.get('quantity')
	request.session['product'] = request.POST.get('product')
	if int(request.session['product']) == 1:
		request.session['price'] = 20
	if int(request.session['product']) == 2:
		request.session['price'] = 30
	if int(request.session['product']) == 3:
		request.session['price'] = 5
	if int(request.session['product']) == 4:
		request.session['price'] = 50
	request.session['amount'] = int(request.session['price'])*int(request.session['quantity'])
	request.session['totalamount']+= int(request.session['amount'])
	request.session['totalquantity']+=int(request.session['quantity'])

	return redirect('/amadon/checkout/')

def checkout(request):
	return render(request, 'checkout.html')

