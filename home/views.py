# -*- coding: utf-8 -*-

# __author__ = 'feng'

from django.shortcuts import render_to_response
from common import function

# 主页
def index(request, cat_id=1, id=1):
    detail = function.get_detail() # 获取公司logo，标题简介等内容
    cats = function.get_cats() # 获取所有分类
    cat_name, articles = function.get_articles(request, cat_id) # 获取某一分类的文章列表
    article = function.get_article(request, id) # 获取一篇文章的内容
    allvar = {
        'detail': detail,
        'cats': cats,
        'cat_name': cat_name,
        'articles': articles,
        'article': article,
    }
    return render_to_response('home/test.html', allvar)