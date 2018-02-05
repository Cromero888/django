# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
	count = 0
	context= {
		'randomword':get_random_string(length=14),
		'count': count

	}
	if 'count' in request.session:
		request.session['count'] += 1
		# return HttpResponse('new count=%s' % request.session['count'])
	else:
		request.session['count'] = 1
		# return HttpResponse('No count in session. Setting to 1')
	return render(request,"index.html", context)

def reset(request):
	request.session.flush()
	return redirect('/')