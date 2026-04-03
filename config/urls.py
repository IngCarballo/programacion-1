"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# Este archivo centraliza las rutas principales del proyecto.
# Desde aquí se decide qué módulos responderán a cada prefijo de URL.
urlpatterns = [
    # Ruta del panel administrativo de Django.
    path('admin/', admin.site.urls),

    # Incluye las rutas definidas en la app `core` bajo el prefijo `/api/`.
    path('api/', include('core.urls')),

    # Expone el esquema OpenAPI de la aplicación.
    # Este esquema describe formalmente la API y luego puede ser usado por Swagger.
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Muestra una interfaz visual para explorar y probar la API desde el navegador.
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
