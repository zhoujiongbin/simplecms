# -*- coding: utf-8 -*-

# __author__ = 'feng'

from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^test/$', views.test, name='test'),
    url(r'^sign1/$', views.sign, name='sign'),
     url(r'^login/$', views.login, name='sign'),
]