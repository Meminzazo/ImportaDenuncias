# Importación de Denuncias a Firebase

Este proyecto permite importar datos de denuncias desde un archivo CSV a una base de datos en tiempo real de Firebase (Realtime Database). El script procesa el archivo CSV, filtra las columnas necesarias y sube los datos en lotes al nodo correspondiente en Firebase.

## Características
- Procesa archivos CSV que contienen información de denuncias.
- Filtra y selecciona las columnas relevantes para su importación.
- Sube los datos a Firebase Realtime Database en lotes para manejar grandes volúmenes de datos de manera eficiente.

## Configuración

### Requisitos
1. **Python 3.7 o superior.**
2. **Credenciales válidas de Firebase.** El archivo JSON con las credenciales de tu base de datos debe ser descargado desde tu consola de Firebase.
3. **Archivo CSV con los datos de las denuncias.**

### Moficar estos valores con datos validos:### Y DESCARGAR LAS CREDENCIALES:
cred = credentials.Certificate(config("FIREBASE_CREDENTIALS"))

firebase_admin.initialize_app(cred, {
    'databaseURL': config("FIREBASE_URL")
})

### Y DESCARGAR LAS CREDENCIALES:
appubicacion-firebase-adminsdk.json
