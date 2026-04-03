# Contexto de trabajo

Este repositorio contiene una serie de 10 trabajos practicos para desarrollar un proyecto completo con backend en Django + Django REST Framework y frontend en React.

La idea general del recorrido es construir una aplicacion web de forma progresiva, entendiendo que cada TP agrega una capa nueva sobre el trabajo anterior.

## Estructura del repositorio

Todo el proyecto se trabaja en un unico repositorio.

Esto implica que:

- el backend y el frontend viven dentro del mismo repositorio,
- la documentacion tambien queda versionada en el mismo lugar,
- y cada TP continua sobre el trabajo ya realizado, sin crear repositorios nuevos para cada parte del sistema.

La estructura esperada es de tipo monorepo. Por ejemplo:

```text
proyecto/
  config/
  core/
  frontend/
  docs/
  tp0.md
  tp1.md
  ...
```

## Objetivo general

Construir una aplicacion full stack con las siguientes etapas:

1. Preparacion del backend.
2. Modelado de datos y creacion de la API.
3. Gestion de usuarios y autenticacion con JWT.
4. Documentacion y testing del backend.
5. Creacion del frontend en React.
6. Maquetado responsive de las vistas.
7. Integracion de autenticacion en frontend.
8. Conexion completa entre frontend y backend.
9. Implementacion del flujo funcional del sistema.
10. Despliegue de la API en la nube.

## Orden mejorado de los trabajos practicos

### TP1
Puesta en marcha del backend con Django y DRF.

### TP2
Modelado de datos, base de datos y API CRUD.

### TP3
Usuarios, roles y autenticacion con JWT.

### TP4
Documentacion y pruebas del backend.

### TP5
Creacion del frontend con React.

### TP6
Maquetado de vistas con Bootstrap.

### TP7
Autenticacion y proteccion de rutas en React.

### TP8
Conexion completa del frontend con la API.

### TP9
Flujo funcional completo del sistema.

### TP10
Despliegue de la aplicacion y documentacion final.

## Criterios de redaccion para los TP

Cada trabajo practico debe incluir:

- Un objetivo claro.
- Una breve explicacion de para que sirve lo que se esta haciendo.
- Requisitos previos si corresponden.
- Pasos ordenados.
- Comandos concretos cuando aplique.
- Entregables esperados.
- Continuidad con el TP siguiente.

## Criterios pedagogicos

- Explicar no solo que se hace, sino tambien por que se hace.
- Evitar mezclar demasiados conceptos nuevos en un mismo TP si no es necesario.
- Introducir primero la version final de autenticacion del proyecto antes de escribir pruebas profundas.
- Mantener consistencia entre backend, frontend, integracion y despliegue.

## Comandos base del backend

```bash
python -m venv venv
source venv/bin/activate
pip install django djangorestframework django-cors-headers drf-spectacular
pip freeze > requirements.txt
django-admin startproject config .
python manage.py startapp core
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Base de datos elegida

Para este recorrido se va a usar PostgreSQL como base de datos principal del proyecto.

Motivos:

- Es una opcion muy comun y solida en proyectos Django.
- Tiene muy buena integracion con el ecosistema del framework.
- Es una eleccion frecuente en entornos reales y de despliegue.
- Evita parte de la configuracion extra que suele aparecer con MySQL.

Durante el TP1 Django puede trabajar con SQLite por defecto para validar que el proyecto arranca correctamente. A partir del TP2 se migra la configuracion a PostgreSQL como base principal del sistema.

## Comandos base para PostgreSQL y autenticacion JWT

```bash
pip install psycopg[binary]
pip install djangorestframework-simplejwt
python manage.py makemigrations
python manage.py migrate
python manage.py test
```

## Comandos base del frontend

```bash
npx create-react-app frontend
cd frontend
npm install
npm install bootstrap react-router-dom
npm start
```

## Buenas practicas generales

- Usar ramas por funcionalidad, por ejemplo `feature/nombre-de-la-tarea`.
- Hacer commits pequenos y descriptivos.
- No subir el archivo `.env` al repositorio.
- Mantener actualizado el `README.md`.
- Documentar endpoints y decisiones tecnicas importantes.
- Probar cada etapa antes de pasar al siguiente TP.

## Intencion del material

La nueva version de los TP debe sentirse como una guia de trabajo progresiva. Cada archivo tiene que ayudar al estudiante a entender:

- que estamos construyendo,
- en que etapa del proyecto estamos,
- que comandos debe ejecutar,
- y que resultado deberia obtener al final.
