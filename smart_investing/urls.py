from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('api/', include('users.urls')),  # Incluir URLs de la aplicación
]
