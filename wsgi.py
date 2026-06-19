"""
WSGI config for stacks project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

# from finflow.otel_config import configure_opentelemetry

load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stacks.settings")


# configure_opentelemetry()

application = get_wsgi_application()
