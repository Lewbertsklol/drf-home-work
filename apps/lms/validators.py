import re
from rest_framework.exceptions import ValidationError


class ForbiddenUrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value is None:
            return
        pattern = re.compile(
            r"https?://(?!(www.youtube|youtube|m.youtube)\.(com|ru|net)/)\S+"
        )
        tmp_value = dict(value).get(self.field)
        urls = re.findall(pattern, tmp_value)
        if urls:
            raise ValidationError("Поле содержит запрещенные ссылки")
