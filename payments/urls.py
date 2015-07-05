from django.conf.urls import patterns, url

from payments import views

urlpatterns = patterns('',
	url(r'^$', views.charge),
)