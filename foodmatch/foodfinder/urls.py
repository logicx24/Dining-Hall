from django.conf.urls import patterns, url
from foodfinder import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^index/$', views.index, name='index'),
		url(r'^register/$', views.register, name='register'),
		url(r'^login/$', views.user_login, name='user_login'),
		url(r'^logout/$', views.user_logout, name='user_logout'),
		url(r'^home/$', views.home, name='home'),
		url(r'^settings/$', views.settings, name='settings'),
		)