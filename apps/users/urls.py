from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views


urlpatterns = [
    path('register/', views.UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=()), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=()), name='token'),

    path('payments/', views.PaymentListAPIView.as_view()),
]
