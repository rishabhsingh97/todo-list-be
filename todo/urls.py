from django.urls import path, include
from .views import ToDoListAPIView, ToDoDetailAPIView, UserRegistrationView, UserLoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView, name='register'),
    path('login/', UserLoginView, name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('todos/', ToDoListAPIView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', ToDoDetailAPIView.as_view(), name='todo-detail'),
    
]