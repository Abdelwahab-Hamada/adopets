import os
import django

from pets.routing import application
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

application=get_default_application()

# application = get_asgi_application()
