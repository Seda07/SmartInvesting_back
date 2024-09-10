from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('api/', include('users.urls')),  # Incluye las rutas definidas en users.urls
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Ruta para obtener tokens (inicio de sesión)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Ruta para refrescar el token de acceso
]
