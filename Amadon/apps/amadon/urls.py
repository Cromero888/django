from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^amadon/checkout/',views.checkout),
	url(r'^buy/', views.buy),
	url(r'^reset/', views.reset),
	url(r'^amadon/', views.index),
	url(r'^', views.start)
]