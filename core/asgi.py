import os
import django

from pets.routing import application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

application=application

# application = get_asgi_application()
