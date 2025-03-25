from .views import UserRegistrationAPIView, UserLoginAPIView, TaskCreateAPIView
from django.urls import path, include

urlpatterns = [
    path('user/registration/', UserRegistrationAPIView.as_view()),
    path('user/login/', UserLoginAPIView.as_view()),
    path('task/', TaskCreateAPIView.as_view()),
    path('task/<int:id>/', TaskCreateAPIView.as_view())
]