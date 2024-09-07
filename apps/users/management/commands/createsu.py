from django.core.management import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **options):
        get_user_model().objects.create_superuser('admin', 'admin@localhost', 'admin')
