from django.urls import path
from .views import User_CreateSerializer, UserCreateAPIView

urlpatterns = [

    path('api/v1/register/', UserCreateAPIView.as_view(), name='register-user'),
]
