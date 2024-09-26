from django.urls import path

from .views import PaymentCreateAPIView, PaymentlistAPIView

urlpatterns = [
    path("", view=PaymentlistAPIView.as_view(), name="payment_list"),
    path("create/", view=PaymentCreateAPIView.as_view(), name="payment_create"),
]
