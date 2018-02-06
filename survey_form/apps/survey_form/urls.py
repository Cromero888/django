from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^result/', views.result),
	url(r'^surveys/process/', views.process),
	url(r'^$', views.index)
]