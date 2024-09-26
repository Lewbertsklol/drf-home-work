from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views


urlpatterns = [
    path("register/", views.UserCreateAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(permission_classes=()), name="login"),
    path(
        "token/refresh/", TokenRefreshView.as_view(permission_classes=()), name="token"
    ),
    path("subs/", views.SubscriptionListAPIView.as_view()),
    path("subs/create/", views.SubscriptionCreateAPIView.as_view()),
    path("subs/destroy/<int:pk>/", views.SubscriptionDestroyAPIView.as_view()),
]
