from django.urls import path
from .views import CreateUser

app_name = "accounts"

urlpatterns = [
    path("register/", CreateUser.as_view(), name="signup")
]
