from django.conf.urls import patterns, url
from foodfinder import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^register/$', views.register, name='register'),
		url(r'^login/$', views.user_login, name='login'),)