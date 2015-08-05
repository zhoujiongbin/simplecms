#!usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from admin.user.models import User
from datetime import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from functools import wraps
import base64

def test(request):
    return render_to_response('sign.html', context_instance=RequestContext(request))


def index(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.session.get('username', False):
            return func(request, *args, **kwargs)
        else:
            return render_to_response('login.html', context_instance=RequestContext(request))
    return wrapper

def login(request):
    if request.method == 'POST':
        user = User.objects.get(account = request.POST['account'])
        str = request.POST['account']+request.POST['password']
        if user.password == base64.b64encode(str.encode(encoding='utf-8')):
            request.session['username'] = request.POST['account']
            str = '<script>window.history.go(-1)</script>'
            return HttpResponse(str)
        else:
            str = '<script>alert("密码或账号错误");window.history.go(-1)</script>'
            return HttpResponse(str)

@index
def sign(request):
    if request.method == 'POST':
        str = request.POST['account'] + request.POST['password']
        u = User()
        print(str)
        u.account = request.POST['account']
        u.email = request.POST['email']
        u.password = base64.b64encode(str.encode(encoding='utf-8'))
        print(u.account)
        try:
            u.save()
            str = '<script>alert("注册成功");window.location.href="http://127.0.0.1:8000/login";</script>'
            return HttpResponse(str)
        except Exception as e:
            return HttpResponseRedirect('.')
    else:
        print(request.session['username'])
        return render_to_response('error.html')

def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/')

