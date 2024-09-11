from django.contrib.auth import get_user_model
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Payment
from .serializers import PaymentSerializer, UserSerializer


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('course', 'lesson', 'payment_option')
    ordering_fields = ('date',)


class UserCreateAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = []
