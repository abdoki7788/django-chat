from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/chat/<slug:slug>/", consumers.ChatConsumer.as_asgi()),
]