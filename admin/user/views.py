#!usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from admin.user.models import User
from datetime import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
import base64

def login(request):
    if request.POST:
        user = User.objects.get(account = request.POST['account'])
        str = request.POST['account']+request.POST['password']
        if user.password == base64.b64encode(str.encode(encoding='utf-8')):
            request.session['username'] = request.POST['account']
            return HttpResponseRedirect(reverse('admin_index'))
        else:
            str = '<script>alert("密码或账号错误");window.history.go(-1)</script>'
            return HttpResponse(str)
    else:
        return render_to_response('admin/user/login.html', context_instance=RequestContext(request))

def register(request):
    if request.POST:
        str = request.POST['account'] + request.POST['password']
        u = User()
        u.account = request.POST['account']
        u.email = request.POST['email']
        u.password = base64.b64encode(str.encode(encoding='utf-8'))
        try:
            u.save()
            str = '<script>alert("注册成功, 返回登录");window.location.href="/admin/user/login";</script>'
            return HttpResponse(str)
        except Exception:
            return HttpResponseRedirect(reverse('register'))
    else:
        return render_to_response('admin/user/register.html', context_instance=RequestContext(request))

def logout(request):
    del request.session['username']
    return HttpResponseRedirect(reverse('login'))

