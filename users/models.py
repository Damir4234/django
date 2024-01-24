from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    country = models.CharField(
        max_length=50, verbose_name='страна', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(
        upload_to='users/', verbose_name='аватар', **NULLABLE)
    verification_code = models.CharField(
        max_length=10, verbose_name='код подтверждения', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('email',)
