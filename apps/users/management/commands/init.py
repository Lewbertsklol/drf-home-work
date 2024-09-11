from django.core.management import BaseCommand, call_command
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from apps.lms.models import Course, Lesson


class Command(BaseCommand):
    help = 'Creates all needed fixterues'

    def handle(self, *args, **options):
        if not get_user_model().objects.filter(username='superuser'):
            call_command('createsuperuser')

        actions = (
            ('moderator group creation', Group.objects.create(name='moderator')),
            ('init courses', course := Course.objects.create(
                name='Тестовый курс',
                user=get_user_model().objects.get(username='superuser')
            )),
            ('init lessons', Lesson.objects.create(
                course=course,
                name='Тестовый урок',
            )),
        )
        for action in actions:
            print(f'Done {action[0]}')
