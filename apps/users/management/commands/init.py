from django.core.management import BaseCommand, call_command
from django.contrib.auth import get_user_model

from apps.users.models import Payment
from apps.lms.models import Course, Lesson


class Command(BaseCommand):
    help = 'Create fixterues'

    def handle(self, *args, **options):
        # call_command('createsu')
        user = get_user_model().objects.first()
        Payment.objects.create(
            user=user,
            date='2022-01-01',
            summ=1000,
            course=(course := Course.objects.create(name='Тестовый курс')),
            payment_option='card'
        )
        Payment.objects.create(
            user=user,
            date='2022-01-01',
            summ=100,
            lesson=Lesson.objects.create(
                name='Тестовый урок',
                course=course
            ),
            payment_option='cash'
        )
