from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Payment, Subscription


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    subscriptions = serializers

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        return get_user_model().objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            password=make_password(validated_data["password"]),
        )


class SubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = "__all__"

    def create(self, validated_date):
        user = self.context["request"].user
        course = validated_date["course"]
        return Subscription.objects.create(user=user, course=course)
