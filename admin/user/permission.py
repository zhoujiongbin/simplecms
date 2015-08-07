#!usr/bin/env python
# -*- coding:
from django.http import Http404, HttpResponse, HttpResponseRedirect
from admin.user.models import User
from datetime import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from functools import wraps


def require_login(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.session.get('username', False):
            return func(request, *args, **kwargs)
        else:
            return render_to_response('admin/user/login.html', context_instance=RequestContext(request))
    return wrapper
