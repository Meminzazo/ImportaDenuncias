import pandas as pd
import firebase_admin
from firebase_admin import credentials, db

# Inicializar Firebase Admin SDK con Realtime Database
cred = credentials.Certificate("appubicacion-419723-firebase-adminsdk-2gcz2-b3a3c0fd0b.json")  # Ruta al archivo de credenciales
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://appubicacion-419723-default-rtdb.firebaseio.com/'
})

# Cargar el archivo CSV
file_path = 'Denuncias 2024 Julio-Septiembre - victimasFGJ_acumulado_2024_09.csv'  # Cambia a la ruta donde se encuentra el CSV descargado
df = pd.read_csv(file_path)

# Filtrar las columnas relevantes
df_filtered = df[['categoria_delito', 'delito', 'latitud', 'longitud', 'fecha_hecho', 'hora_hecho']]

# Convertir a una lista de diccionarios para subir a Firebase
data_to_import = df_filtered.to_dict(orient='records')

# Subir los datos a Firebase en lotes de 1000 registros
batch_size = 1000  # Tamaño del lotez
total_records = len(data_to_import)

for start_idx in range(0, total_records, batch_size):
    end_idx = min(start_idx + batch_size, total_records)
    batch = data_to_import[start_idx:end_idx]

    # Crear referencia al nodo "denuncias"
    ref = db.reference('denuncias')

    for record in batch:
        try:
            # Añadir cada registro al nodo "denuncias"
            ref.push(record)
        except Exception as e:
            print(f"Error al importar el registro {record}: {e}")

    print(f"Lote desde {start_idx} hasta {end_idx} procesado exitosamente.")

print("Importación completa.")