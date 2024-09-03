from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.exceptions import AuthenticationFailed
from todo_app.models import Todo
from .serializers import TaskSerializer
from rest_framework import generics
from rest_framework.views import APIView
# or from rest_framework.generics import ListAPIView
from .models import Todo
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class TaskListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def get(self, request, *args, **kwargs):
        return Response({'detail': 'Method "GET" not allowed. Please use POST with credentials.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


