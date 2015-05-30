from django.conf.urls import patterns, include, url
from django.contrib import admin

from penny_for_your_thoughts import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^charge/', views.charge),
    url(r'^login/', views.login_user),
    url(r'^logout/', views.logout_user),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^thought/', include('thoughts.urls')),
)
