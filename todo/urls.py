from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet, ToDoDetailView, UserRegistrationView, UserLoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'todos', ToDoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView, name='register'),
    path('login/', UserLoginView, name='login'),
    path('todos/<int:pk>/', ToDoDetailView, name='todo-detail'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]