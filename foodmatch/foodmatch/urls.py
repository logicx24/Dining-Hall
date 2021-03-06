from django.conf.urls import patterns, include, url
from foodfinder import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodmatch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^foodfinder/', include('foodfinder.urls')),
    url(r'^$', views.redirection, name='redirection'),
)
