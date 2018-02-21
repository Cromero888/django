from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^addcourse/', views.addcourse),
	url(r'^remove/(?P<id>\d+)', views.remove),
	url(r'^deletecourse/(?P<id>\d+)', views.deletecourse),
	url(r'^', views.index),
]