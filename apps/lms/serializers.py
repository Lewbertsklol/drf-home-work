from rest_framework import serializers

from apps.users.serializers import UserSerializer
from apps.payments.models import Payment

from .models import Course, Lesson
from .validators import ForbiddenUrlValidator


class LessonSerializer(serializers.ModelSerializer):
    is_bougth = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [
            ForbiddenUrlValidator(field="name"),
            ForbiddenUrlValidator(field="description"),
        ]

    def get_is_bougth(self, instance):
        user = self.context["request"].user
        return Payment.objects.filter(lesson=instance, user=user).exists()

    def create(self, validated_data):
        user = self.context["request"].user
        course = validated_data["course"]
        if course.user != user:
            raise serializers.ValidationError("Вы не являетесь владельцем этого курса.")
        return super().create(validated_data)


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    subscription = serializers.SerializerMethodField()
    is_bougth = serializers.SerializerMethodField()

    def get_is_bougth(self, instance):
        user = self.context["request"].user
        return Payment.objects.filter(course=instance, user=user).exists()

    def get_subscription(self, instance):
        return instance.subscribers.filter(user=self.context["request"].user).exists()

    def get_count_lessons(self, instance):
        return instance.lessons.count()

    class Meta:
        model = Course
        fields = "__all__"
        validators = [
            ForbiddenUrlValidator(field="name"),
            ForbiddenUrlValidator(field="description"),
        ]
