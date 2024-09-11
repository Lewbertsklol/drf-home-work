from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = 'Creates superuser'

    def handle(self, *args, **options):
        get_user_model().objects.create_superuser(
            username='superuser',
            email=input('Enter email: ').strip(),
            password=input('Enter password: ').strip()
        )
        print('Superuser created')
