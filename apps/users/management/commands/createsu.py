from django.core.management import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **options):
        User = get_user_model()
        User.objects.create_superuser('admin', 'admin@localhost', 'admin')
