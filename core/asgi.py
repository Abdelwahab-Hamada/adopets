import os
import django

from channels.routing import get_default_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

application=Cling(get_default_application())

# application = get_asgi_application()
