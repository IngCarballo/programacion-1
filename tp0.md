# TP0

## Guia inicial de herramientas de trabajo

Este documento no es un trabajo practico en si mismo. Su objetivo es presentar las herramientas que vamos a usar durante el desarrollo del proyecto, explicar para que sirve cada una y dejar una base comun para toda la cursada.

Durante los siguientes TP vamos a trabajar con backend, frontend, base de datos, control de versiones y consumo de APIs. Para eso necesitamos familiarizarnos con un conjunto de herramientas que nos van a acompañar durante todo el proceso.

## Objetivo

Conocer las herramientas principales del entorno de trabajo y entender en que momento del proyecto se usa cada una.

## Herramientas que vamos a usar

### 1. DBeaver

`DBeaver` es una herramienta grafica para administrar bases de datos.

La vamos a usar para:

- conectarnos a PostgreSQL,
- crear o inspeccionar bases de datos,
- ver tablas y relaciones,
- ejecutar consultas SQL,
- revisar si las migraciones de Django se aplicaron correctamente.

En este proyecto resulta especialmente util para visualizar la base de datos sin depender solamente de la terminal.

Sitio oficial:

- `https://dbeaver.io/`

### 2. Postman

`Postman` es una herramienta para probar APIs.

La vamos a usar para:

- enviar peticiones `GET`, `POST`, `PUT` y `DELETE`,
- probar endpoints del backend,
- enviar credenciales o tokens JWT,
- revisar respuestas JSON,
- verificar si una ruta protegida responde correctamente.

Es muy util para testear la API antes de conectarla al frontend.

Sitio oficial:

- `https://www.postman.com/`

### 3. GitHub Desktop

`GitHub Desktop` es una herramienta visual para trabajar con Git y GitHub.

La vamos a usar para:

- clonar repositorios,
- ver archivos modificados,
- hacer commits,
- cambiar de rama,
- publicar cambios en GitHub.

Aunque muchos comandos tambien pueden hacerse por terminal, GitHub Desktop ayuda a entender mejor el flujo de versionado, sobre todo al comienzo.

Sitio oficial:

- `https://desktop.github.com/`

### 4. Visual Studio Code

`Visual Studio Code` es el editor de codigo que vamos a usar durante la cursada.

La vamos a usar para:

- escribir codigo en Python, JavaScript y JSX,
- editar configuraciones del proyecto,
- navegar rapidamente por carpetas y archivos,
- usar la terminal integrada,
- instalar extensiones utiles para Django, React y formateo.

Es una de las herramientas mas usadas en desarrollo web por su flexibilidad y por la gran cantidad de extensiones disponibles.

Sitio oficial:

- `https://code.visualstudio.com/`

## Recomendacion general

Antes de comenzar con el TP1, es recomendable instalar todas estas herramientas y verificar que abren correctamente en tu equipo.

No hace falta dominarlas por completo desde el primer dia, pero si es importante entender para que sirve cada una:

- `Visual Studio Code` para programar,
- `GitHub Desktop` para versionar,
- `DBeaver` para trabajar con la base de datos,
- `Postman` para probar la API.

## Agente: OpenCode

`OpenCode` es un asistente de IA orientado al trabajo con proyectos de software.

Puede ayudar a leer codigo, explicar errores, proponer cambios y asistir durante el desarrollo del proyecto.

En esta cursada se usara como una herramienta complementaria para acompanar el trabajo practico, pero no reemplaza la comprension del codigo ni la documentacion oficial.

La guia completa de instalacion, configuracion y uso se encuentra en `opencode.md`.
