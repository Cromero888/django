from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^process/', views.process),
	url(r'^clear/', views.clear),
	url(r'^$', views.index)
]