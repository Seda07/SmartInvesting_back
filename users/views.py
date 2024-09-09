from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                # Aquí deberías generar tokens JWT o cualquier otro mecanismo de autenticación
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
