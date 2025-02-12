import os
import json

# Ruta de la carpeta donde están las imágenes
carpeta_banners = './assets/banners'

# Obtener los archivos de la carpeta
imagenes = []

# Recorrer los archivos en la carpeta
for archivo in os.listdir(carpeta_banners):
    # Filtrar solo las imágenes con extensiones .jpg, .jpeg, .png
    if archivo.lower().endswith(('.webp')):
        imagenes.append(os.path.join(carpeta_banners, archivo))

# Crear un diccionario con el array de imágenes
datos = {'imagenes': imagenes}

# Guardar el JSON en un archivo
with open('./assets/banners/imagenes.json', 'w') as json_file:
    json.dump(datos, json_file, indent=4)

print("JSON generado exitosamente.")
