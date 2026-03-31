# Guia de uso y configuracion de OpenCode

## Que es OpenCode

`OpenCode` es una herramienta de asistencia con IA orientada al desarrollo de software.

Puede usarse para:

- leer y explicar codigo,
- sugerir cambios,
- ayudar a encontrar errores,
- generar estructuras iniciales,
- y acompanar el desarrollo de un proyecto tecnico.

Su uso en esta cursada es complementario. Sirve como apoyo, pero no reemplaza la comprension del codigo ni la documentacion oficial de las herramientas que se estan usando.

## Formas de uso

OpenCode puede utilizarse de distintas maneras segun la necesidad del usuario.

### 1. OpenCode Desktop

Es la aplicacion independiente. Integra editor, terminal y chat en una misma interfaz.

Es una buena opcion para trabajar en proyectos grandes o cuando se quiere tener todo el flujo en un solo lugar.

### 2. Extension para Visual Studio Code

Si ya se usa Visual Studio Code como entorno principal, se puede instalar la extension de OpenCode.

Esto permite:

- abrir un panel de chat lateral,
- pedir ayuda contextual sobre el codigo,
- y usar edicion inline para cambios rapidos.

### 3. Interfaz de linea de comandos

Tambien puede utilizarse desde terminal, lo cual es util para consultas rapidas o para quienes prefieren un flujo mas cercano a la consola.

## Configuracion del entorno

## Conexion con el LLM de la facultad

1. Acceder al portal:
   - `https://ai.cloud.um.edu.ar`

2. Iniciar sesion con las credenciales institucionales.

3. Obtener una API Key:
   - ir a la seccion de ajustes o cuenta,
   - generar una nueva clave,
   - guardarla en un lugar seguro,
   - no compartirla con otras personas.

## Configuracion en OpenCode

Pasos generales:

1. Abrir la configuracion de OpenCode.
2. Ir a la seccion de proveedores.
3. Crear un proveedor personalizado.
4. Completar los datos de conexion.

Ejemplo de configuracion:

- ID del proveedor: `um-ia`
- Nombre visible: `Gemma Facultad (UM)`
- URL base: `https://ai.cloud.um.edu.ar/api/v1`
- API Key: la clave generada en el portal
- Modelo: `gemma3-4b` o `gpt-oss-20b`

Despues de guardar la configuracion, se puede seleccionar el modelo desde la interfaz principal de OpenCode.

## Recomendacion sobre modos de uso

OpenCode suele ofrecer distintos modos de trabajo.

- `Plan`: pensado para conversar, pedir explicaciones, generar ideas o revisar enfoques.
- `Build`: pensado para crear o modificar archivos cuando el modelo soporta ese flujo.

Como recomendacion general, conviene empezar por `Plan` cuando se esta configurando la herramienta o cuando se necesita una explicacion antes de editar codigo.

## GitHub Copilot

Si el estudiante tiene acceso a GitHub Copilot, tambien puede integrarlo como proveedor adicional o usarlo en paralelo para autocompletado.

En general:

- se obtiene mediante GitHub Student Developer Pack,
- se vincula desde la seccion de proveedores o desde Visual Studio Code,
- y se usa principalmente para sugerencias de codigo en tiempo real.

## Otros modelos complementarios

Tambien se pueden agregar otros proveedores, como OpenAI o Google, si el entorno lo permite.

Esto puede ser util cuando se quiere comparar respuestas o consultar modelos diferentes para tareas complejas.

## Buenas practicas de uso

- No compartir API keys.
- No copiar respuestas sin entenderlas.
- Verificar siempre el codigo sugerido por la IA.
- Contrastar con documentacion oficial cuando haya dudas.
- Usar la herramienta como apoyo, no como reemplazo del aprendizaje.

## Nota de seguridad

Si una API Key queda expuesta o se sospecha que fue compartida, se recomienda revocarla desde el portal correspondiente y generar una nueva.
