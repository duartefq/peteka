from django.conf.urls import patterns, url

from department import views

urlpatterns = patterns('',
		url(r'^$', views.index, name="index"),
	)