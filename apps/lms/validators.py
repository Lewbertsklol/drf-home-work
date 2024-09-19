import re
from rest_framework.exceptions import ValidationError


class ForbiddenUrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        if tmp_value is None:
            return
        pattern = re.compile(
            r"https?://(?!(www.youtube|youtube|m.youtube)\.(com|ru|net)/)\S+"
        )
        if re.findall(pattern, tmp_value):
            raise ValidationError("Поле содержит запрещенные ссылки")
