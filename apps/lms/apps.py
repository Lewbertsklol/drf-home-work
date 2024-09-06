from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.lms'
    verbose_name = _('Курс')
