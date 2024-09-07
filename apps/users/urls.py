from django.urls import path

from . import views


urlpatterns = [
    path('', views.PaymentListAPIView.as_view()),
]
