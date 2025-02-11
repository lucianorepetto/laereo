from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import json
import re

# Configura el WebDriver
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Puedes eliminar esta línea si quieres ver el navegador

driver = webdriver.Chrome(options=options)

# Accede a la URL
url = "https://www.google.com/search?sca_esv=619d14064cab1183&cs=1&output=search&kgmid=/g/11cnn3y3p2&q=L%27AEREO+repair+station&shndl=30&source=sh/x/kp/local/m1/1&kgs=984817f3a549a7a3&sei=6oarZ4HqIerl5NoPrs_z8Aw#lrd=0x9432bb556127576b:0x62b407059bc8343b,1,,,,"
driver.get(url)

# Espera a que el contenedor de las reseñas esté presente en la página
try:
    # Esperamos a que el contenedor de reseñas (por ejemplo, review-dialog-list) esté visible
    review_dialog_list = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".review-dialog-list"))
    )

    print("Elemento 'review-dialog-list' encontrado.")
    
    # Simulamos el scroll hasta que se carguen todas las reseñas
    previous_reviews_count = 0
    while True:
        # Desplazamos hacia abajo en el contenedor de reseñas
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", review_dialog_list)
        
        # Esperamos un poco para que las nuevas reseñas carguen
        time.sleep(2)

        # Verificamos el número de reseñas cargadas
        reviews = review_dialog_list.find_elements(By.CSS_SELECTOR, ".Jtu6Td")
        current_reviews_count = len(reviews)

        # Si no hay nuevas reseñas, terminamos el scroll
        if current_reviews_count == previous_reviews_count:
            break
        
        # Actualizamos la cantidad de reseñas cargadas
        previous_reviews_count = current_reviews_count

    # Obtiene el contenido completo de 'review-dialog-list'
    review_dialog_html = review_dialog_list.get_attribute("outerHTML")

    # Guarda el HTML completo en un archivo .html
    # with open("review_dialog.html", "w", encoding="utf-8") as f:
    #     f.write(review_dialog_html)
    # print("El contenido de 'review-dialog-list' se ha guardado en 'review_dialog.html'.")
    
    # Procesar el HTML de las reseñas
    soup = BeautifulSoup(review_dialog_html, "html.parser")

    reviews_data = []

    # Buscar todas las reseñas dentro del contenedor
    reviews = soup.select(".gws-localreviews__google-review")

    name_ = ".TSUbDb"
    review_text_ = ".Jtu6Td"
    stars_ = ".PuaHbe span"

    for review in reviews:
        # Extraer el nombre de la persona
        name = review.select_one(name_).get_text(strip=True) if review.select_one(name_) else "Unknown"
        
        # Extraer las estrellas
        rating_span = review.select_one(stars_)
        rating = rating_span['aria-label'] if rating_span else "Calificación no disponible"
        if rating != "Calificación no disponible":
            match = re.search(r'Calificación:\s*(\d+)', rating)
            rating = match.group(1)
        
        # Extraer el texto de la reseña
        review_text = review.select_one(review_text_).get_text(strip=True) if review.select_one(review_text_) else ""
        
        # Crear un diccionario con la información de la reseña
        review_info = {
            "name": name,
            "stars": rating,
            "review_text": review_text
        }

        # Añadir la reseña al listado
        reviews_data.append(review_info)

    # Guardar los datos extraídos en un archivo JSON
    with open("reviews.json", "w", encoding="utf-8") as json_file:
        json.dump(reviews_data, json_file, ensure_ascii=False, indent=4)

    print("El archivo 'reviews.json' ha sido generado correctamente.")

except Exception as e:
    print(f"Error al encontrar los elementos o al obtener el HTML: {e}")

# Cierra el navegador
driver.quit()
