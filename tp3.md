  
***Trabajo Práctico N°3***  
***Gestión de usuarios y control de sesiones mediante cookies***

**Actividades**

1. Crear la app usuario.  
2. Migrar el modelo usuario de la app inicial a la nueva app usuario. Asegurarse que el modelo usuario herede de abstract user.  
3. Crear serializers, views y url para el modelo usuario.  
4. Crear el login, logout y register.  
5. Agregar los permisos de usuario para los modelos usando “**from rest\_framework import permissions, viewsets**”.  
6. Agregar en el settings del proyecto en **INSTALLED\_APPS** el nombre del la app usuario. Y en **REST\_FRAMEWORK** agregar:  
   'DEFAULT\_AUTHENTICATION\_CLASSES': \[  
           'rest\_framework.authentication.SessionAuthentication',  
   \],  
   y al final agregar **AUTH\_USER\_MODEL \= 'nombreAppUser.Users'**  
7. En el url del proyecto agregar las urls de la app usuario: **path('api/user/', include('nombreAppUser.urls')),**  
8. Probar que funcione.