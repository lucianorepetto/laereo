from PIL import Image
from pathlib import Path
from moviepy.editor import VideoFileClip
import os

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
convert_to_mp4(raiz)