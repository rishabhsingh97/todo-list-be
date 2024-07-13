from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet, register_user, login_user

router = DefaultRouter()
router.register(r'todos', ToDoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
]