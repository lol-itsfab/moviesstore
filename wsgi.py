"""
WSGI config for moviesstore project on PythonAnywhere.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the Python path
path = '/home/yourusername/moviesstore'  # Replace 'yourusername' with your actual PythonAnywhere username
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviesstore.settings_production')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
