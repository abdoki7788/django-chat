from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path("", views.index, name="index"),
    path("c/<slug:slug>/", views.room, name="room"),
    path("add_friend/", views.add_friend, name="add_friend"),
]