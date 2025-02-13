from PIL import Image
from pathlib import Path
from moviepy.editor import VideoFileClip
import os

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


raiz = os.path.join(os.path.dirname(__file__), '..', 'assets')
convert_to_webp(raiz)