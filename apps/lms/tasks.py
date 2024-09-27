from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from apps.lms.models import Course


@shared_task(name="send_email")
def send_email(*, course_id: int, users_id: list):
    course = Course.objects.get(id=course_id)
    User = get_user_model()
    recipient_list = User.objects.filter(id__in=users_id).values_list(
        "email", flat=True
    )
    send_mail(
        subject=f"{course.name} have been changed",
        message=f"Check out new changes in {course.name}",
        from_email=None,
        recipient_list=recipient_list,
        fail_silently=False,
    )
