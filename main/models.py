from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    '''основная модель пользователя'''
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'  # Используйте email для аутентификации
    REQUIRED_FIELDS = []  # Уберите 'username' из обязательных полей
