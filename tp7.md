# 📝 Trabajo Práctico N°7: Login, Registro y Control de Acceso

## 🎯 Objetivo

Implementar un sistema de autenticación en React con **registro**, **login**, **logout** y **control de acceso a la Home**, utilizando validaciones hardcodeadas.

---

## 📦 Entregables

- Proyecto React con login, logout y registro funcionando  
- Acceso a la Home solo para usuarios autenticados  
- Repositorio con ramas organizadas y commits claros

---

## 🛠️ Actividades

### 1\. Crear y preparar la rama de trabajo

- Crear una nueva rama, por ejemplo:  
  `feature/auth-system`.

---

### 2\. Implementar contexto de autenticación

- Crear `AuthContext` para manejar el estado del usuario  
- Incluir funciones `login`, `logout` y `register` con datos hardcodeados

---

### 3\. Crear componente de Login

- Formulario de usuario y contraseña  
- Validación contra datos hardcodeados  
- Redirección a la Home si es exitoso

---

### 4\. Crear componente de Registro

- Formulario para registrar nuevo usuario  
- Agregar nuevo usuario al estado (no persistente)

---

### 5\. Crear componente de Logout

- Botón para cerrar sesión y redirigir al Login

---

### 6\. Proteger la ruta Home

- Crear componente `ProtectedRoute`  
- Redirigir al Login si el usuario no está autenticado

---

## ✅ Resultado Esperado

- Usuario puede registrarse, iniciar y cerrar sesión  
- Acceso a la Home solo si está autenticado  
- Navegación controlada y coherente  
- Código organizado y versionado correctamente

---
