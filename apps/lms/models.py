from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    name = models.CharField(_('Название'), max_length=255)
    preview = models.ImageField(_('Превью'), blank=True, null=True)
    description = models.TextField(_('Описание'), blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Курс')
        verbose_name_plural = _('Курсы')


class Lesson(models.Model):
    name = models.CharField(_('Название'), max_length=255)
    preview = models.ImageField(_('Превью'), blank=True, null=True)
    description = models.TextField(_('Описание'), blank=True, null=True)
    video_url = models.TextField(_('Ссылка на видео'), blank=True, null=True)
    course = models.ForeignKey('lms.Course', on_delete=models.CASCADE, related_name='lessons')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Урок')
        verbose_name_plural = _('Уроки')
