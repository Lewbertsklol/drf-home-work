from rest_framework import serializers

from apps.users.serializers import UserSerializer, SubscriptionSerializer
from .models import Course, Lesson
from .validators import ForbiddenUrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [
            ForbiddenUrlValidator(field="name"),
            ForbiddenUrlValidator(field="description"),
        ]

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

    def get_subscription(self, instance):
        return self.context["request"].user in instance.subscribers.all()

    def get_count_lessons(self, instance):
        return instance.lessons.count()

    class Meta:
        model = Course
        fields = "__all__"
        validators = [
            ForbiddenUrlValidator(field="name"),
            ForbiddenUrlValidator(field="description"),
        ]
