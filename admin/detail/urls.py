# -*- coding: utf-8 -*-

# __author__ = 'feng'

from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
     url(r'^admin/edit',views.index, name='edit')
]