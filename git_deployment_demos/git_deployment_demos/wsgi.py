# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'git_deployment_demos.settings')
#
# application = get_wsgi_application()

# git_deployment_demos/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

# Set the Django settings module for the WSGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'git_deployment_demos.settings')

# Get the Django WSGI application
django_application = get_wsgi_application()


def application(environ, start_response):
    # Pass the environment and start_response callable to the Django application
    return django_application(environ, start_response)


