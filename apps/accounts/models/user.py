from django.contrib.auth.models import AbstractBaseUser

from django.db import models
from accounts.models.user_manager import CustomUserManager
from uuid import uuid4
class Users(AbstractBaseUser):
    id = models.UUIDField(primary_key = True, default = uuid4, null = False, editable = False)
    email = models.EmailField(unique=True, null = False, blank = False)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
