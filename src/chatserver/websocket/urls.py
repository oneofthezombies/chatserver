from django.urls import re_path
import chatapp.consumers


urlpatterns = [
    re_path(r'^room/(?P<room_name>[\w-]+)/consumer$', chatapp.consumers.ChatConsumer.as_asgi())
]
