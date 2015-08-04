from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from admin.cat.models import Cat
from django.db import models

def article(request):
    return HttpResponse('article')

@csrf_exempt
def add(request):
    article_title = request.POST['article_title']
    article_author = request.POST['article_author']
    article_content = request.POST['article_content']
    article_cat_id = request.POST['article_id']
    article=Article()
    article.article_title=article_title
    article.article_author=article_author
    article.article_content=article_content
    article.article_cat_id=article_cat_id
    article.save()
    return HttpResponse('save seccess')



#编辑文章页面
def index(request):
    query_set = Cat.objects.all()
    cat = []  #保存全部分类
    # 获取一级分类
    for item in query_set:
        cat.append({'cat_name':item.cat_name, 'cat_id':item.cat_id})
    return render(request,'add.html',{'cat':cat})


#后台查看、修改文章的页面
@csrf_exempt
def check(request):
    id=request.POST['id']
    article=Article.objects.get(id=id)
    return render(request,'check.html',{'article':article})


#删除文章
@csrf_exempt
def delete(request):
    id=request.POST['id']
    article=Article.objects.get(id=id)
    article.delete()
    return HttpResponse('delete seccuss')

#修改文章
@csrf_exempt
def edit(request):
    id=request.POST['id']
    article=Article.objects.get(id=id)
    article.article_title=request.POST['article_title']
    article.article_author=request.POST['article_author']
    article.article_content=request.POST['article_content']
    article.publish_time= models.DateTimeField(auto_now_add=True)
    article._do_update()
    return HttpResponse('edit success')


def list(request):
    article=[]
    query_set = Article.objects.all()
    # 获取一级分类
    for item in query_set:
        article.append({'id':item.id,'article_title':item.article_title, 'article_content':item.article_content})
    return render(request,'add.html',{'article':article})







