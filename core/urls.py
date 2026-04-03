# `path` es la función que permite declarar rutas dentro de una app Django.
from django.urls import path

# Importamos la vista que va a responder cuando se acceda a la ruta definida abajo.
from .views import HealthCheckView


# `urlpatterns` es la lista principal de rutas de esta app.
# Cada elemento conecta una URL con una vista concreta.
urlpatterns = [
    # Esta ruta expone el endpoint `/health/`.
    # `as_view()` convierte la clase en una vista utilizable por Django.
    # `name` define un identificador interno para referenciar esta ruta.
    path('health/', HealthCheckView.as_view(), name='health-check'),
]
