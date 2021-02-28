from django.urls import re_path
from . import views


app_name = 'chatapp'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^join/$', views.join, name='join'),
    re_path(r'^room/(?P<room_name>[\w-]+)/$', views.room, name='room')
]
