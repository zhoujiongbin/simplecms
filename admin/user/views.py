#!usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from admin.user.models import User
from datetime import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
import base64

def index(request):
    return render_to_response('admin/user/login.html', context_instance=RequestContext(request))

def login(request):
    if request.method == 'POST':
        user = User.objects.get(account = request.POST['account'])
        str = request.POST['account']+request.POST['password']
        if user.password == base64.b64encode(str.encode(encoding='utf-8')):
            return HttpResponseRedirect('admin_index')
        else:
            str = '<script>alert("密码或账号错误");window.history.go(-1)</script>'
            return HttpResponse(str)

def sign(request):
    if request.method == 'POST':
        str = request.POST['account'] + request.POST['password']
        #str = str.encode('utf-8')
        u = User()
        u.account = request.POST['account']
        u.email = request.POST['email']
        u.password = base64.b64encode(str.encode(encoding='utf-8'))
        u.power = 0
        try:
            u.save()
            str = '<script>alert("注册成功");window.location.href="http://127.0.0.1/login";</script>'
            return HttpResponse(str)
        except Exception:
            return HttpResponseRedirect('.')

def logout(request):
    pass

