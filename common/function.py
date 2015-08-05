# -*- coding: utf-8 -*-

# __author__ = 'feng'
from admin.cat.models import Cat
from admin.article.models import Article
from admin.detail.models import Detail

# 根据ID获取分类名
def get_cat(id):
    query_set = Cat.objects.get(cat_id=id)
    cat_name = query_set.cat_name
    return cat_name

# 获取所有分类
def get_cats():
    query_set = Cat.objects.all()
    cats = [] # 用来储存搜索结果
    # 获取一级分类
    for item in query_set:
        father_id = item.cat_father
        if father_id == 0:
            cats.append({
                'cat_father': item.cat_father,
                'cat_name': item.cat_name,
                'cat_url':'/'+str(item.cat_id),  # 分类的链接url
                'cat_id': item.cat_id,
            })
    return cats

# 获取公司logo路径，公司标题，公司简介
def get_detail():
    query_set = Detail.objects.get(id=1)
    detail = {
        'logo_path': query_set.logo_path,
        'title': query_set.title,
        'introduction': query_set.introduction,
    }
    return detail

# 获取所有文章
def get_all_articles():
    article_list = []
    query_set = Article.objects.all()
    for item in query_set:
        article_list.append({
            'article_id': item.id,
            'article_title': item.article_title,
            'article_author': item.article_author,
            'article_content': item.article_content,
            'publish_time': item.publish_time,
            'cat_name': get_cat(int(item.article_cat_id_id)),
            'article_url': '/'+str(item.article_cat_id_id)+'/'+str(item.id),  # 文章的链接url
            'article_edit_url': '/edit/'+str(item.id),
        })
    return article_list

# 根据分类获取文章列表
def get_articles(request, cat_id=1):
    article_list = []   # 储存搜索结果
    query_set = Article.objects.filter(article_cat_id_id=cat_id)
    cat_name = get_cat(cat_id)
    for item in query_set:
        article_list.append({
            'article_id': item.id,
            'article_title': item.article_title,
            'article_author': item.article_author,
            'article_content': item.article_content,
            'publish_time': item.publish_time,
            'cat_name': get_cat(item.article_cat_id_id),
            'article_url': '/'+str(cat_id)+'/'+str(item.id),  # 文章的链接url
            'article_edit_url': '/edit/'+str(item.id),
        })
    return cat_name, article_list


# 获取文章详情内容
def get_article(id=1):
    query_set = Article.objects.get(id=id)
    article = {
        'article_id': query_set.id,
        'article_title': query_set.article_title,
        'article_author': query_set.article_author,
        'article_content': query_set.article_content,  # 文章内容
        'publish_time': query_set.publish_time,
    }
    return article
