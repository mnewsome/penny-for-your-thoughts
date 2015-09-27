from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='account_index'),
)