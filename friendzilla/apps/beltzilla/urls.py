from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^user/(?P<id>\d+)/', views.user),
	url(r'^remove/(?P<id>\d+)/', views.remove),
	url(r'^add/(?P<id>\d+)/', views.addfriend),

	url(r'^$', views.friends),
]