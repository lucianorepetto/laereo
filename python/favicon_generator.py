import os
from PIL import Image

def generate_favicons(input_image_path, output_folder):
    # Verifica que la carpeta de salida exista
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Abre la imagen de entrada
    img = Image.open(input_image_path)

    # Lista de tamaños para los favicons
    sizes = [16, 32, 48, 64, 128, 256]

    # Genera favicons en los tamaños especificados
    favicon_paths = []
    for size in sizes:
        output_path = os.path.join(output_folder, f"favicon_{size}x{size}.png")
        img.resize((size, size)).save(output_path)
        favicon_paths.append(output_path)
    
    return favicon_paths

def update_html_with_favicons(html_file, favicon_paths):
    # Lee el contenido del archivo HTML línea por línea
    with open(html_file, 'r', encoding='utf-8') as file:
        html_lines = file.readlines()

    # Elimina las líneas que contienen rel="icon"
    html_lines = [line for line in html_lines if 'rel="icon"' not in line]

    # Encuentra la primera aparición de </head> para insertar las nuevas etiquetas antes
    head_end_index = next((i for i, line in enumerate(html_lines) if '</head>' in line), None)

    # Inserta las nuevas etiquetas de favicon justo antes de </head>
    favicon_links = ""
    for path in favicon_paths:
        size = os.path.basename(path).split('_')[1].split('x')[0]
        favicon_links += f'\n    <link rel="icon" href="./{os.path.relpath(path, start=os.path.dirname(html_file)).replace(os.sep, "/")}" sizes="{size}x{size}"/>'
    favicon_links += f'\n'

    if head_end_index is not None:
        # Inserta los favicons antes de </head>
        html_lines.insert(head_end_index, favicon_links)

    # Guarda el archivo HTML actualizado
    with open(html_file, 'w', encoding='utf-8') as file:
        file.writelines(html_lines)

def main():
    # Rutas relativas utilizando os.path.join
    raiz = os.path.join(os.path.dirname(__file__), '..', 'assets', 'favicons')  # Carpeta para los favicons
    input_image_path = os.path.join(os.path.dirname(__file__), 'favicon.png')  # Ruta de la imagen de entrada
    html_file = os.path.join(os.path.dirname(__file__), '..', 'index.html')  # Ruta del archivo HTML

    # Generar los favicons
    favicon_paths = generate_favicons(input_image_path, raiz)
    
    # Actualizar el archivo HTML con los favicons
    update_html_with_favicons(html_file, favicon_paths)

if __name__ == "__main__":
    main()
