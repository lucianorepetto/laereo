import PIL
from PIL import Image
from pathlib import Path
from moviepy.editor import VideoFileClip
import os


def file_to_webp(source):
    destination = source.with_suffix(".webp")

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination

def convert_just_one_folder(raiz):
    for filename in os.listdir(raiz):
        path = os.path.join(raiz, filename)

        if os.path.isfile(path) and any(
                filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']):
            try:
                img = Image.open(path)
                webp_path = os.path.splitext(path)[0] + ".webp"
                img.save(webp_path, "WEBP")
                print(f"Converted {path} to {webp_path}")
            except Exception as e:
                print(f"Error converting {path}: {e}")


def convert_to_webp(root_dir):
    print(root_dir)
    for root, dirs, files in os.walk(root_dir):

        for filename in files:
            path = os.path.join(root, filename)

            if any(filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']):
                try:
                    img = Image.open(path)
                    webp_path = os.path.splitext(path)[0] + ".webp"
                    img.save(webp_path, "WEBP")

                    # Borra la original
                    os.remove(path)

                    print(f"Converted {path} to {webp_path}")
                except Exception as e:
                    print(f"Error converting {path}: {e}")

def convert_to_mp4(root_dir):
    print(f"Starting conversion in directory: {root_dir}")
    
    # Extensiones de video que se van a convertir
    video_extensions = ['.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v']
    
    # Recorre todos los archivos en el directorio
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            path = os.path.join(root, filename)
            # Comprueba si el archivo tiene una extensión de video que queremos convertir
            if any(filename.lower().endswith(ext) for ext in video_extensions):
                
                try:
                    # Convierte a MP4
                    with VideoFileClip(path) as video:
                        mp4_path = os.path.splitext(path)[0] + ".mp4"
                        video.write_videofile(mp4_path, codec='libx264', audio_codec='aac')
                    
                    # Borra el archivo original después de la conversión
                    os.remove(path)
                    print(f"Converted {path} to {mp4_path}")
                    
                except Exception as e:
                    print(f"Error converting {path}: {e}")


raiz = os.path.join(os.path.dirname(__file__), '..', 'assets')
# raiz = 'C:/Users/lucia/OneDrive/Documentos/Mis Documentos/Pages/AdimensionalShopV3/src/images'
# convert_to_webp(raiz)
convert_to_mp4(raiz)
# convert_just_one_folder(raiz)