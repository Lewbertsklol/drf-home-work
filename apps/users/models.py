from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('Номер телефона'), max_length=20, blank=True, null=True)
    city = models.CharField(_('Город'), max_length=255, blank=True, null=True)
    avatar = models.ImageField(_('Аватарка'), blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
