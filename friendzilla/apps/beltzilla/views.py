# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import *
from ..logreg.models import User

# Create your views here.

def friends(request):
	Friend.objects.filter(friend1=request.session['user_id']) or Friend.objects.filter(friend2=request.session['user_id'])
	context = {
		'su1': Friend.objects.filter(friend1=request.session['user_id']),
		'su2': Friend.objects.filter(friend2=request.session['user_id']),
		'friends': Friend.objects.filter(friend1=request.session['user_id']).select_related() or Friend.objects.filter(friend2=request.session['user_id']).select_related(),
		# 'stuff1': Friend.objects.select_related('friend1').get(id=3).friend2,
		'users': User.objects.exclude(id=request.session['user_id']),
		'me': User.objects.get(id=request.session['user_id']).first_name,
	}
	return render(request, 'table.html', context)

def user(request, id):
	context = {
		'user': User.objects.get(id=id)
	}
	return render(request, 'user.html', context)


def addfriend(request, id):
	friend = Friend.objects.create(friend1=User.objects.get(id=request.session['user_id']), friend2=User.objects.get(id=id))
	friend.save()
	return redirect('/friends/')

def remove(request, id):
	friend = Friend.objects.get(id=id)
	friend.delete()
	return redirect('/friends/')