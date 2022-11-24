from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profiles/', default="profile.png")
    last_seen = models.DateTimeField(auto_now_add=True)