"""
WSGI config for ad_agency project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Load .env only in non-production environments
if os.environ.get("DEBUG", "1") != "0":
    try:
        import dotenv
        dotenv.load_dotenv(dotenv_path=".env.dev")
    except ImportError:
        pass  # dotenv not installed — ignore silently

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ad_agency.settings')

application = get_wsgi_application()
