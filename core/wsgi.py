"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

###addiotanl info 

path = './Render-Test/core/'
path = '/home/usitingshit/deploy_course_work/'
if path not in sys.path:
  sys.path.append(path)


##os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

application = get_wsgi_application()
