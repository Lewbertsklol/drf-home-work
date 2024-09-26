from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Payment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payments"
    )
    payment_url = models.URLField(verbose_name=_("Ссылка на оплату"))
    course = models.ForeignKey(
        "lms.Course", on_delete=models.DO_NOTHING, null=True, blank=True
    )
    lesson = models.ForeignKey(
        "lms.Lesson", on_delete=models.DO_NOTHING, null=True, blank=True
    )

