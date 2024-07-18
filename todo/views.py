from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import ToDo
from .serializers import ToDoSerializer, UserRegistrationSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class ToDoListAPIView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

class ToDoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
@permission_classes([AllowAny]) 
def UserRegistrationView(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny]) 
def UserLoginView(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
