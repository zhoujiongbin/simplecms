"""
WSGI config for simplecms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simplecms.settings")
#
# application = get_wsgi_application()
import os
import sys

sys.stdout = sys.stderr

from os.path import abspath, dirname, join
from site import addsitedir

from django.core.handlers.wsgi import WSGIHandler

sys.path.insert(0, abspath(join(dirname(__file__), "../")))
sys.path.insert(0, abspath(join(dirname(__file__), ". . /. . /")))

os.environ["DJANGO_SETTINGS_MODULE"] = "simplecms.settings"

application = WSGIHandler()