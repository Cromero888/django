# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import datetime

# Create your views here.
def index(request):
	context={
	"time": datetime.datetime.now()
	}
	return render(request, 'index.html', context)
