# -*- coding: utf-8 -*-

# __author__ = 'feng'

from django.conf.urls import include, url

from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^test/$', views.test, name='test'),
    url(r'^sign1/$', views.sign, name='sign'),
     url(r'^login/$', views.login, name='sign'),
=======
    url(r'^$|login/', views.index, name='login')
>>>>>>> 109a2d7cfb6da8dd012149ef55523708162f3481
]