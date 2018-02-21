from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^adduser/', views.adduser),
	url(r'^add/', views.add),
	url(r'^users/', views.users),
	url(r'^edit/(?P<id>\d+)', views.edit),
	url(r'^edituser/(?P<id>\d+)', views.edituser),
	url(r'^deleteuser/(?P<id>\d+)', views.deleteuser),
	url(r'^show/(?P<id>\d+)', views.show),
	url(r'^', views.index),
]