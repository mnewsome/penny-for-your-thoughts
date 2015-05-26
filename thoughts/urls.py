from django.conf.urls import patterns, url

from thoughts import views

urlpatterns = patterns('',
    url(r'^(?P<thought_id>\d+)/$', views.show, name='show'),
)