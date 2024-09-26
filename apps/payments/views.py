from rest_framework import generics

from .serializers import PaymentSerializer
from .models import Payment


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer


class PaymentlistAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)
