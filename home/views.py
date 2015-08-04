from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.http import HttpResponse
from admin.detail.models import Detail
from admin.cat.models import Cat
from admin.article.models import Article

# 主页
def index(request, cat_id=1, id=1):
    detail = get_detail() # 获取公司logo，标题简介等内容
    cats = get_cats() # 获取所有分类
    cat_name, articles = get_articles(request, cat_id) # 获取某一分类的文章列表
    article = get_article(request, id) # 获取一篇文章的内容
    allvar = {
        'detail': detail,
        'cats': cats,
        'cat_name': cat_name,
        'articles': articles,
        'article': article,
    }
    return render_to_response('home/test.html', allvar)

# 获取公司logo路径，公司标题，公司简介
def get_detail():
    query_set = Detail.objects.get(id=1)
    detail = {
        'logo_path':query_set.logo_path, 
        'title':query_set.title,
        'introduction':query_set.introduction
    }
    return detail

# 获取所有分类
def get_cats():
    query_set = Cat.objects.all()
    cats = [] # 用来储存搜索结果
    # 获取一级分类
    for item in query_set:
        father_id = item.cat_father
        if father_id == 0:
            cats.append({
                'cat_name': item.cat_name,
                'cat_url':'/'+str(item.cat_id),  # 分类的链接url
                'cat_id': item.cat_id
            })
    return cats

# 根据ID获取分类名
def get_cat(id):
    query_set = Cat.objects.get(cat_id=id)
    cat_name = query_set.cat_name
    return cat_name

# 根据分类获取文章列表
def get_articles(request, cat_id=1):
    article_list = [] # 储存搜索结果
    query_set = Article.objects.filter(article_cat_id_id = cat_id)
    cat_name = get_cat(cat_id)
    for item in query_set:
        article_list.append({
            'article_title':item.article_title,
            'article_url':'/'+str(cat_id)+'/'+str(item.id) # 文章的链接url
        })
    # return render_to_response('home/article_list.html', {'articles':article_list, })
    return cat_name, article_list


# 获取文章详情内容
def get_article(request, id):
    query_set = Article.objects.get(id = id)
    article = {
        'article_title': query_set.article_title,
        'article_author': query_set.article_author,
        'article_content': query_set.article_content,  # 文章内容
        'publish_time': query_set.publish_time,
    }
    return article