from django.shortcuts import render

from rest_framework import viewsets
from .models import ToDo
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ToDoSerializer, UserSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated] 

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def todo_detail(request, pk):
    try:
        todo_item = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return Response({'error': 'Todo item does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ToDoSerializer(todo_item)
    return Response(serializer.data)


