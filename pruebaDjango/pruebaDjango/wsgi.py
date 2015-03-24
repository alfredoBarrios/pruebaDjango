"""
WSGI config for pruebaDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pruebaDjango.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

a=10
B=10
print "hola"
