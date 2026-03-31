## **PROMT:**

El proyecto actual esta manteniendo las sesiones y los roles usando las cookies del navegador, del propio framework de django. Necesitamos cambiarlo para implementar jwt, y usar el manejo de sesiones mediante headers vía postman, Diseña los cambios necesarios e implementarlos

## 

## 

## **🔐 Autenticación JWT en Django con DRF – Guía paso a paso**

### **✅ Paso 1: Crear un proyecto y app en Django**

bash  
CopiarEditar  
`django-admin startproject myproject`  
`cd myproject`  
`python manage.py startapp myapp`

---

### **✅ Paso 2: Instalar dependencias necesarias**

Instalá Django REST Framework y Simple JWT:

bash  
CopiarEditar  
`pip install djangorestframework djangorestframework-simplejwt`

---

### **✅ Paso 3: Configurar `settings.py`**

#### **a) Agregá las apps al `INSTALLED_APPS`:**

python  
CopiarEditar  
`INSTALLED_APPS = [`  
    `...`  
    `'rest_framework',`  
    `'myapp',`  
`]`

#### **c) Configurá la zona horaria y otras opciones si lo necesitás:**

python  
CopiarEditar  
`LANGUAGE_CODE = 'es-ar'`  
`TIME_ZONE = 'America/Argentina/Buenos_Aires'`

---

### **✅ Paso 4: Crear el modelo de usuario (opcional)**

Si vas a usar el modelo por defecto, podés saltear esto. Si no:

python  
CopiarEditar  
`# myapp/models.py`  
`from django.contrib.auth.models import AbstractUser`  
`from django.db import models`

`class CustomUser(AbstractUser):`  
    `pass`

Y en `settings.py`:

python  
CopiarEditar  
`AUTH_USER_MODEL = 'myapp.CustomUser'`

---

### **✅ Paso 5: Crear las vistas y rutas para login con JWT**

#### **a) Crear `urls.py` dentro de la app (si no lo tenés)**

python  
CopiarEditar  
`# myapp/urls.py`  
`from django.urls import path`  
`from rest_framework_simplejwt.views import (`  
    `TokenObtainPairView,`  
    `TokenRefreshView,`  
`)`

`urlpatterns = [`  
    `path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),`  
    `path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),`  
`]`

#### **b) Agregá las rutas al `urls.py` del proyecto:**

python  
CopiarEditar  
`# myproject/urls.py`  
`from django.contrib import admin`  
`from django.urls import path, include`

`urlpatterns = [`  
    `path('admin/', admin.site.urls),`  
    `path('', include('myapp.urls')),`  
`]`

---

### **✅ Paso 6: Crear una vista protegida con JWT**

python  
CopiarEditar  
`# myapp/views.py`  
`from rest_framework.views import APIView`  
`from rest_framework.response import Response`  
`from rest_framework.permissions import IsAuthenticated`

`class ProtectedView(APIView):`  
    `permission_classes = [IsAuthenticated]`

    `def get(self, request):`  
        `return Response({'message': f'Hola, {request.user.username}. Estás autenticado con JWT!'})`

Y agregala a `myapp/urls.py`:

python  
CopiarEditar  
`from .views import ProtectedView`

`urlpatterns += [`  
    `path('api/protected/', ProtectedView.as_view(), name='protected'),`  
`]`

---

### **✅ Paso 7: Crear un superusuario para probar**

bash  
CopiarEditar  
`python manage.py makemigrations`  
`python manage.py migrate`  
`python manage.py createsuperuser`

---

### **✅ Paso 8: Probar todo con Postman o cURL**

#### **1\. Obtener token:**

**POST** a `/api/token/` con:

json  
CopiarEditar  
`{`  
  `"username": "admin",`  
  `"password": "tu_contraseña"`  
`}`

Respuesta:

json  
CopiarEditar  
`{`  
  `"access": "eyJ0eXAiOiJKV1QiLCJh...",`  
  `"refresh": "eyJ0eXAiOiJKV1QiLCJh..."`  
`}`

#### **2\. Usar token en una vista protegida:**

**GET** a `/api/protected/` con header:

makefile  
CopiarEditar  
`Authorization: Bearer TU_TOKEN_ACCESS`  