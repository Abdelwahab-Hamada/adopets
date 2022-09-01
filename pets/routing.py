from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from .tokenAuthMiddleware import TokenAuthMiddleware
from .consumers import Consumer


application = ProtocolTypeRouter({
    "websocket": TokenAuthMiddleware(URLRouter([
        path("pets/", Consumer.as_asgi()),
    ]))
})