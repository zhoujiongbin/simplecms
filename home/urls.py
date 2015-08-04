# -*- coding: utf-8 -*-

# __author__ = 'feng'

from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cat_id>\d+)$', views.index, name='cat'),
    url(r'^(?P<cat_id>\d+)/(?P<id>\d+)', views.index, name='article'),
]