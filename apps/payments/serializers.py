from rest_framework import serializers
from .models import Payment

from apps.lms.serializers import CourseSerializer, LessonSerializer
from apps.users.serializers import UserSerializer
from .services import create_product


class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    payment_url = serializers.URLField(read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"

    def create(self, validated_data):
        course = validated_data.get("course")
        lesson = validated_data.get("lesson")
        user = self.context["request"].user
        if course and lesson:
            raise serializers.ValidationError("Only one field is required")
        if product := (course or lesson):
            payment_url = create_product(product)
            return Payment.objects.create(
                user=user, payment_url=payment_url, course=course, lesson=lesson
            )
        else:
            raise serializers.ValidationError("Course or lesson required")
