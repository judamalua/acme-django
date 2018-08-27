"""
WSGI config for acmeDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from polls.wsgi import PollsApplication

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acmeDjango.settings')

application = get_wsgi_application()


application = HelloWorldApplication(application)
