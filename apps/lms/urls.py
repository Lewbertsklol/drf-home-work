from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

router = DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', views.LessonListAPIView.as_view()),
    path('lessons/<int:pk>/', views.LessonRetrieveAPIView.as_view()),
    path('lessons/create/', views.LessonCreateAPIView.as_view()),
    path('lessons/<int:pk>/update/', views.LessonUpdateAPIView.as_view()),
    path('lessons/<int:pk>/delete/', views.LessonDestroyAPIView.as_view()),
]
