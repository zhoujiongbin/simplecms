# -*- coding: utf-8 -*-

# __author__ = 'feng'

from django.conf.urls import include, url

from admin.article import views

urlpatterns = [
    url(r'^article/', views.article, name='article'),  #测试专用
    url(r'^add/', views.add, name='add'),              #添加文章
    url(r'^delete/', views.delete, name='delete'),    #删除文章
    url(r'^edit/', views.edit, name='edit'),           #修改文章
    url(r'^index/', views.index, name='index'),        #编辑文章
    url(r'^check/', views.check, name='check'),        #查看文章
    url(r'^list/', views.list, name='list'),           #文章列表
]