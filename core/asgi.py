import os

from django.core.asgi import get_asgi_application

from pets.routing import application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application=application

# application = get_asgi_application()
