from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from celery import shared_task


@shared_task
def ban_users():
    User = get_user_model()
    users = User.objects.filter(last_login__lt=datetime.now() - timedelta(days=30))
    users.update(is_active=False)
    print(f"Unactive users: {users} banned")
