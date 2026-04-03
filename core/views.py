# `Response` es una utilidad de Django REST Framework.
# Se usa para devolver datos en formato HTTP de manera consistente, por ejemplo JSON.
from rest_framework.response import Response

# `APIView` es la clase base para construir vistas orientadas a API.
# Permite definir métodos como `get`, `post`, `put` o `delete` segun el tipo de petición.
from rest_framework.views import APIView


# Esta clase representa una vista simple de verificación.
# Su objetivo académico es mostrar cómo se define un endpoint en una API REST.
# Al heredar de `APIView`, la clase puede responder a distintos métodos HTTP.
class HealthCheckView(APIView):

    # `get` es el método que se ejecuta cuando el cliente hace una petición GET.
    # El parámetro `request` contiene la información enviada por el cliente.
    # En este caso no se procesa lógica compleja: solo se responde con un mensaje
    # que confirma que el backend está activo.
    def get(self, request):
        return Response({'status': 'ok', 'service': 'django-api'})
