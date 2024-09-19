from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Владелец"),
        on_delete=models.CASCADE,
        related_name="courses",
    )
    name = models.CharField(_("Название"), max_length=255)
    preview = models.ImageField(_("Превью"), blank=True, null=True)
    description = models.TextField(_("Описание"), blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Курс")
        verbose_name_plural = _("Курсы")


class Lesson(models.Model):
    name = models.CharField(_("Название"), max_length=255)
    preview = models.ImageField(_("Превью"), blank=True, null=True)
    description = models.TextField(_("Описание"), blank=True, null=True)
    video_url = models.TextField(_("Ссылка на видео"), blank=True, null=True)
    course = models.ForeignKey(
        "lms.Course", on_delete=models.CASCADE, related_name="lessons"
    )

    @property
    def user(self):
        return self.course.user

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Урок")
        verbose_name_plural = _("Уроки")
