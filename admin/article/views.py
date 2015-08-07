from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from .models import Article
from admin.cat.models import Cat
from django.db import models
from common import function
from admin.user.permission import require_login
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage

# 文章管理页面
@require_login
def article(request):
    article_list = function.get_all_articles()
    return render_to_response('admin/article/article.html', {'article_list': article_list})

# 添加文章

@csrf_exempt
@require_login
def add(request):
    if request.POST:
        title = request.POST['title']
        author = request.POST['author']
        cat_id = request.POST['cat_id']
        publish_time = request.POST['publish_time']
        content = request.POST['content']
        a = Article(article_title=title, article_author=author, publish_time=publish_time, article_content=content, article_cat_id_id=cat_id)
        a.save()
        return HttpResponseRedirect(reverse('article'))
    else:
        cats = function.get_cats()
        return render_to_response('admin/article/article_add.html', {'cats': cats})


# 文章编辑页面
@csrf_exempt
@require_login
def edit(request, article_id):
    if request.POST:
        title = request.POST['title']
        author = request.POST['author']
        cat_id = request.POST['cat_id']
        publish_time = request.POST['publish_time']
        content = request.POST['content']
        a = Article.objects.filter(id=int(article_id))
        a.update(article_title=title, article_author=author, publish_time=publish_time, article_content=content, article_cat_id_id=cat_id)
        return HttpResponseRedirect(reverse('article'))
    else:
        article_detail = function.get_article(article_id)
        cats = function.get_cats()
        return render_to_response('admin/article/article_editor.html', {'cats': cats, 'article': article_detail})

# 删除文章
@csrf_exempt
@require_login
def delete(request, article_id):
    a = Article.objects.get(id=article_id)
    a.delete()
    return HttpResponse('<script>alert("删除成功");window.location.href="/admin/article"</script>')


#关键字搜索文章
def search_by_page(request):
    each_page=2
    if 'q' in request.GET and request.GET['q']:
          q = request.GET['q']
    article_list=function.get_article_search(q)
    paginator = Paginator(article_list,each_page)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('admin/article/article.html',{'article_list': contacts,'q':q,'paginator':paginator})






