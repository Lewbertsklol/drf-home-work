from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(_('Имя пользователя'), max_length=255)
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


class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    date = models.DateTimeField(verbose_name=_('Дата платежа'))
    course = models.ForeignKey('lms.Course', on_delete=models.CASCADE, related_name='payments', blank=True, null=True)
    lesson = models.ForeignKey('lms.Lesson', on_delete=models.CASCADE, related_name='payments', blank=True, null=True)
    summ = models.FloatField(verbose_name=_('Сумма платежа'))
    payment_option = models.CharField(
        verbose_name=_('Опция платежа'),
        max_length=255,
        choices=(('card', 'Карта'), ('cash', 'Наличные'))
    )

    class Meta:
        verbose_name = _('Платеж')
        verbose_name_plural = _('Платежи')

    def __str__(self) -> str:
        return f'{self.user}: {self.summ}'
