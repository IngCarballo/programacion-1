# Trabajo Practico N°2

## Modelado de datos, PostgreSQL y API CRUD inicial

## Objetivo

En este trabajo practico vamos a pasar del proyecto base a una primera version funcional del backend. Para eso vamos a definir las entidades principales del sistema, conectar el proyecto a PostgreSQL y crear los primeros endpoints CRUD de la API.

La idea es que al finalizar ya exista una estructura real de datos y una API inicial sobre la cual despues podamos agregar autenticacion, permisos, pruebas e integracion con el frontend.

## Por que usamos PostgreSQL

Para este proyecto vamos a trabajar con PostgreSQL como base de datos principal.

Es una buena eleccion porque:

- es una base muy usada en proyectos Django,
- tiene muy buena compatibilidad con el framework,
- suele ser una opcion estandar en desarrollo profesional,
- y resulta conveniente tambien para futuros despliegues.

En el TP1 usamos la configuracion inicial por defecto de Django para validar el arranque del proyecto. En este TP ya pasamos a la base de datos definitiva del backend.

## Requisitos previos

Antes de empezar, deberias tener completo el TP1 y ademas:

- PostgreSQL instalado en tu equipo,
- un usuario con permisos para crear bases de datos,
- una base de datos creada para el proyecto, por ejemplo `programacion1_db`.

## Instalacion de PostgreSQL

Si todavia no tenes PostgreSQL instalado, podes hacerlo antes de continuar con este TP.

Documentacion oficial:

- PostgreSQL Downloads: `https://www.postgresql.org/download/`
- Documentacion oficial de PostgreSQL: `https://www.postgresql.org/docs/`

Segun tu sistema operativo:

- macOS: se puede instalar con `Homebrew`.
- Windows: se recomienda usar el instalador oficial de PostgreSQL.
- Linux: se puede instalar desde el gestor de paquetes de la distribucion.

Ejemplo en macOS con Homebrew:

```bash
brew install postgresql
brew services start postgresql
```

Despues de instalarlo, verificar que el servicio este corriendo y que el cliente `psql` este disponible:

```bash
psql --version
```

Si preferis no detallar toda la instalacion en el TP, como minimo debe quedar referenciada la documentacion oficial para que cada estudiante pueda seguir la guia correcta segun su sistema operativo.

## Conexion con DBeaver

Si, es totalmente posible conectar PostgreSQL con DBeaver, y de hecho es una muy buena idea para visualizar tablas, relaciones y datos sin depender solo de la terminal.

Documentacion oficial:

- DBeaver: `https://dbeaver.io/`
- Documentacion de conexiones PostgreSQL en DBeaver: `https://dbeaver.com/docs/dbeaver/Database-driver-PostgreSQL/`

Pasos generales para conectar la base del proyecto en DBeaver:

1. Abrir DBeaver.
2. Crear una nueva conexion.
3. Elegir `PostgreSQL` como motor.
4. Completar los datos de conexion:
   - Host: `localhost`
   - Port: `5432`
   - Database: `programacion1_db`
   - Username: el usuario configurado en PostgreSQL
   - Password: la contrasena correspondiente
5. Probar la conexion.
6. Guardar.

Una vez conectada la base, DBeaver permite:

- ver tablas y columnas,
- ejecutar consultas SQL,
- inspeccionar relaciones,
- revisar los datos cargados por Django,
- y comprobar rapidamente si las migraciones se aplicaron bien.

## Entregables

Al finalizar este TP se espera tener:

- PostgreSQL conectado al proyecto Django,
- modelos principales definidos,
- migraciones aplicadas correctamente,
- serializers creados,
- vistas CRUD iniciales funcionando,
- rutas de API registradas,
- y documentacion basica disponible en Swagger.

## Paso 1: Instalar el conector de PostgreSQL

Con el entorno virtual activado, instalar el paquete necesario:

```bash
pip install psycopg[binary]
```

Luego actualizar el archivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```

## Paso 2: Crear la base de datos en PostgreSQL

Si todavia no existe, crear una base de datos para el proyecto. Esto se puede hacer desde `psql`, pgAdmin o la herramienta que estes usando para administrar PostgreSQL.

Tambien puede hacerse desde DBeaver si ya tenes una conexion creada al servidor PostgreSQL.

Por ejemplo, desde consola:

```sql
CREATE DATABASE programacion1_db;
```

Tambien es recomendable trabajar con un usuario propio del proyecto en lugar de usar el usuario administrador general.

## Paso 3: Configurar `DATABASES` en Django

Abrir `config/settings.py` y reemplazar la configuracion por defecto por una configuracion para PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'programacion1_db',
        'USER': 'postgres',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Estos valores deben adaptarse a la instalacion local de cada estudiante.

## Paso 4: Definir el modelo de datos inicial

Antes de escribir codigo, pensar que entidades necesita la aplicacion.

Como guia general, un sistema de tipo ecommerce o inventario podria incluir modelos como:

- `Category`
- `Product`
- `Stock`
- `Cart`
- `CartItem`
- `Order`
- `OrderItem`

No hace falta implementar toda la logica avanzada todavia, pero si dejar definidos los modelos base con sus relaciones principales.

Se recomienda hacer un diagrama simple y guardarlo en `docs/` o incluirlo en el `README.md`.

## Paso 5: Crear los modelos en `models.py`

En la app correspondiente, crear los modelos seleccionados.

Algunas recomendaciones:

- usar nombres claros,
- definir relaciones con `ForeignKey` o `ManyToManyField` cuando corresponda,
- agregar campos como `created_at` o `updated_at` si ayudan a ordenar el sistema,
- mantener una estructura simple y entendible.

## Paso 6: Crear y aplicar migraciones

Una vez definidos los modelos, ejecutar:

```bash
python manage.py makemigrations
python manage.py migrate
```

Esto transforma los modelos en tablas reales dentro de PostgreSQL.

## Paso 7: Registrar modelos en el admin

En `admin.py`, registrar los modelos principales para poder verlos desde el panel de administracion.

Este paso es util para verificar rapidamente que las tablas existen y que los datos pueden cargarse correctamente.

## Paso 8: Crear serializers

Crear un archivo `serializers.py` dentro de la app y definir los serializers necesarios.

Ejemplo general:

```python
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```

Los serializers permiten convertir objetos de Django a JSON y viceversa, lo cual es esencial para construir la API REST.

## Paso 9: Crear vistas CRUD

En `views.py`, crear vistas usando `ModelViewSet` o la estrategia que se haya definido para el proyecto.

Ejemplo general:

```python
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

Con esto ya se pueden exponer operaciones CRUD basicas sobre un modelo.

## Paso 10: Configurar rutas de la API

En la app, crear o completar `urls.py` con un router de DRF:

```python
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

Luego incluir esas rutas en el archivo principal `config/urls.py`:

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]
```

## Paso 11: Configurar Swagger

Como `drf-spectacular` ya fue instalado en el TP1, ahora se puede terminar de integrar la documentacion.

En `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```

Y en `config/urls.py` agregar:

```python
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
```

## Paso 12: Ejecutar y verificar

Levantar el servidor:

```bash
python manage.py runserver
```

Verificar:

- panel admin: `http://127.0.0.1:8000/admin/`
- API: `http://127.0.0.1:8000/api/`
- Swagger: `http://127.0.0.1:8000/api/docs/`

## Resultado esperado

Al finalizar este trabajo practico deberias tener:

1. el backend conectado a PostgreSQL,
2. una primera estructura de modelos reales,
3. migraciones aplicadas correctamente,
4. endpoints CRUD iniciales funcionando,
5. y una base lista para agregar autenticacion y permisos en el proximo TP.

## Recomendaciones finales

- Hacer pruebas manuales desde el admin y desde Swagger.
- Cargar algunos registros de ejemplo para verificar relaciones.
- Mantener nombres consistentes entre modelos, serializers, vistas y rutas.
- Hacer un commit al finalizar, por ejemplo: `add postgres setup and initial crud api`.

## Proximo paso

En el siguiente trabajo practico vamos a incorporar el sistema de usuarios del proyecto y la autenticacion con JWT para proteger rutas y trabajar con sesiones reales desde la API.
