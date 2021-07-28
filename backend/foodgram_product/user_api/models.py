from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('Электронная почта'),
                              unique=True,
                              max_length=55,
                              blank=False)
    username = models.CharField(unique=True,
                                max_length=30,
                                blank=False,
                                verbose_name='Имя пользователя')
    first_name = models.CharField(max_length=30,
                                  blank=False,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=30,
                                 blank=False,
                                 verbose_name='Фамилия')
    is_subscribed = models.BooleanField()

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
