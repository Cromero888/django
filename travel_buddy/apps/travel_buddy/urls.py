from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^destination/(?P<id>\d+)/', views.destination),
	url(r'^addprocess/', views.addprocess),
	url(r'^add/', views.add),
	url(r'^join/', views.join),
	url(r'^$', views.travels),
]