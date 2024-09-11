from rest_framework import serializers
from django.contrib.auth import get_user_model


# Obtén el modelo de usuario personalizado
CustomUser = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Asegúrate de que el password sea write-only
        }

    def create(self, validated_data):
        # Crear un usuario utilizando el CustomUserManager
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# Serializador de Tokens JWT
class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
