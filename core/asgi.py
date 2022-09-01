import os

from pets.routing import application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application=application

# application = get_asgi_application()
