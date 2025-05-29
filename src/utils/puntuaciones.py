import json
import os
from config.configuracion import ARCHIVO_PUNTUACIONES

class Puntuaciones:
    def __init__(self):
        self.RUTA_PUNTUACIONES = ARCHIVO_PUNTUACIONES

    def guardar_puntuacion(self, nombre, tiempo, nivel):
        try:
            puntuaciones = self.cargar_puntuaciones()
        except:
            puntuaciones = []
        
        nueva_puntuacion = {
            'nombre': nombre,
            'tiempo': tiempo,
            'nivel': nivel
        }
        
        puntuaciones.append(nueva_puntuacion)
        puntuaciones.sort(key=lambda x: x['tiempo'])  # Ordenar por tiempo (menor es mejor)
        
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(self.RUTA_PUNTUACIONES), exist_ok=True)
        
        with open(self.RUTA_PUNTUACIONES, 'w') as archivo:
            json.dump(puntuaciones, archivo, indent=2)

    def cargar_puntuaciones(self):
        try:
            with open(self.RUTA_PUNTUACIONES, 'r') as archivo:
                return json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def obtener_mejores_puntuaciones(self, limite=5):
        puntuaciones = self.cargar_puntuaciones()
        return puntuaciones[:limite]

    def es_record(self, tiempo):
        puntuaciones = self.cargar_puntuaciones()
        if not puntuaciones:
            return True
        return tiempo < puntuaciones[0]['tiempo'] 