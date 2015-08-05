# -*- coding: utf-8 -*-

# __author__ = 'feng'
from django.conf.urls import include, url

from admin.cat import views

urlpatterns = [
    url(r'^$', views.indexView, name='cat_view'),
    url(r'^add/$',views.addCat,name='cat_add'),
    url(r'^edit/(?P<ID>\d+)/$', views.editCat, name='cat_edit'),
    url(r'^delete/(?P<ID>\d+)/$',views.deleteCat,name='cat_delete'),
]