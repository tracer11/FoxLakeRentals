from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractBaseUser):
  email = models.CharFiled(unique=True)
  phone = models.IntField(unique=True)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  date_joined = models.DateTimeField(default=timezone.now)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['phone']

  objects = CustomUserManager()