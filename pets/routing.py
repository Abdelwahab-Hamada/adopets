from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from .tokenAuthMiddleware import TokenAuthMiddleware
from .consumers import Consumer
from dj_static import Cling


django_asgi_app = Cling(get_asgi_application())

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": TokenAuthMiddleware(URLRouter([
        path("pets/", Consumer.as_asgi()),
    ]))
})