from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Creates moderator'

    def handle(self, *args, **options):
        moderator = get_user_model().objects.create(
            username='moderator',
            email=input('Enter email: ').strip(),
            password=make_password(input('Enter password: ').strip())
        )
        moderator.groups.set(
            (Group.objects.get(name='moderator'),)
        )
        print('Moderator created')
