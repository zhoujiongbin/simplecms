# -*- coding: utf-8 -*-

# __author__ = 'feng'

from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.article, name='article'),                 # 文章管理界面
    url(r'^add/', views.add, name='article_add'),              # 添加保存文章
    url(r'^delete/(?P<article_id>\d+)/', views.delete, name='article_delete'),              # 删除文章
    url(r'^edit/(?P<article_id>\d+)/', views.edit, name='article_edit'),           # 修改文章

]