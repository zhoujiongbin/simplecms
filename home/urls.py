# -*- coding: utf-8 -*-

# __author__ = 'feng'

from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, {'template': 'home/index.html'}, name='index'),
    url(r'^(?P<cat_id>\d+)$', views.index, {'template': 'home/index.html'}, name='cat'),
    url(r'^(?P<cat_id>\d+)/(?P<article_id>\d+)', views.index, {'template': 'home/article_detail.html'}, name='article'),
]