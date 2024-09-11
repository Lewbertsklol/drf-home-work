from rest_framework import serializers

from apps.users.serializers import UserSerializer
from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        
    def create(self, validated_data):
        user = self.context['request'].user
        course = validated_data['course']
        if course.user != user:
            raise serializers.ValidationError("Вы не являетесь владельцем этого курса.")
        return super().create(validated_data)


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    def get_count_lessons(self, instance):
        return instance.lessons.count()

    class Meta:
        model = Course
        fields = '__all__'
