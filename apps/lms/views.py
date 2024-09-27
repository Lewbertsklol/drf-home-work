from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.users.permissions import IsModerator
from .permissions import IsOwner
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from .paginators import Pagination
from .tasks import send_email


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = Pagination

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action == "create":
            permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action in ("update", "partial_update"):
            permission_classes = [IsModerator | IsOwner]
        elif self.action == "destroy":
            permission_classes = [IsOwner, ~IsModerator]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save()
        course = self.get_object()
        subscribers = course.subscribers.all().values_list("user", flat=True)
        send_email.delay(course_id=course.id, users_id=list(subscribers))


# Lessons
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = Pagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner | IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner, ~IsModerator]
