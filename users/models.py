from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user = models.CharField(max_length=150, default="")