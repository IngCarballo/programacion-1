# `serializers` es el módulo de Django REST Framework que permite transformar
# datos de Python en formatos que una API puede devolver, como JSON, y también
# validar información que llega desde el cliente.
from rest_framework import serializers


# Esta clase define un serializador simple.
# Un serializador describe la estructura de los datos que se van a enviar o recibir.
# En este caso se usa para representar la respuesta del endpoint de health check.
class HealthCheckSerializer(serializers.Serializer):

    # `status` y `service` son campos de texto.
    # Estos atributos indican qué claves tendrá la respuesta y qué tipo de dato
    # se espera en cada una.
    status = serializers.CharField()
    service = serializers.CharField()
