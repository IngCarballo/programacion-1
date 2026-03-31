# 📝 Trabajo Práctico N°9: Conexión del Frontend con el Backend

## 🎯 Objetivo

Conectar el frontend realizado en React con el backend existente, de modo que todas las vistas accedan a los datos reales desde la base de datos mediante una API REST. Además, se debe implementar un sistema de autenticación y manejo de sesión para garantizar privacidad y control de acceso.

---

## 📦 Entregables

- Aplicación React conectada exitosamente al backend  
- Consumo de endpoints reales para login, logout, registro y vistas protegidas  
- Manejo de sesión con almacenamiento seguro del token o cookie  
- Protección de rutas y validación de autenticación en el frontend  
- Código organizado y funcional en un repositorio

---

## 🛠️ Actividades

### 1\. Preparar el entorno

- Verificar que tanto el backend como el frontend estén corriendo correctamente  
- Confirmar la URL base de la API (por ejemplo, [http://localhost:8000/api](http://localhost:8000/api))  
- Configurar variables de entorno si es necesario

---

### 2\. Conectar el login real

- Reemplazar la lógica de MSW o autenticación hardcodeada  
- Usar fetch o axios para hacer POST a /api/login/  
- Almacenar el token o cookie proporcionada por el backend  
- Redirigir al usuario a la Home si el login es exitoso

---

### 3\. Conectar el registro

- Agregar o adaptar el formulario de registro  
- Hacer POST a /api/register/ con los datos del nuevo usuario  
- Notificar al usuario si el registro fue exitoso o si hubo errores

---

### 4\. Manejo de sesión y logout

- Verificar la sesión del usuario con el backend  
- Implementar logout (por ejemplo, con POST a /api/logout/ o borrado del token)  
- Limpiar los datos del usuario al cerrar sesión

---

### 5\. Proteger rutas privadas

- Restringir el acceso a ciertas vistas si el usuario no está autenticado  
- Usar context o hooks para mantener el estado global de autenticación  
- Redirigir automáticamente al login si se intenta acceder a una ruta protegida

---

### 6\. Conectar las demás vistas

- Obtener los datos dinámicamente desde la API REST (productos, usuarios, movimientos, etc.)  
- Hacer peticiones GET, POST, PUT o DELETE según lo requiera cada vista  
- Mostrar la información actualizada de la base de datos en la interfaz

---

## ✅ Resultado Esperado

- Frontend React completamente funcional y conectado al backend  
- Navegación protegida según el estado de sesión del usuario  
- Formulario de login y registro operativos con verificación real  
- Vistas que muestran datos reales de la base de datos a través de la API

---

## 📚 Recursos y documentación

- Documentación de fetch: [https://developer.mozilla.org/en-US/docs/Web/API/Fetch\_API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)  
- Axios (alternativa): [https://axios-http.com/docs/intro](https://axios-http.com/docs/intro)  
- Protección de rutas en React: [https://reactrouter.com/en/main/start/tutorial\#protecting-routes](https://reactrouter.com/en/main/start/tutorial#protecting-routes)  
- Uso de context: [https://reactjs.org/docs/context.html](https://reactjs.org/docs/context.html)  
- Buenas prácticas de autenticación en frontend: [https://auth0.com/docs](https://auth0.com/docs)
