import argparse
import sys
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json
from urllib.parse import urlencode
import os

# Función única para realizar la búsqueda y extraer datos
def obtener_y_extraer_datos(keyword, nombre_fichero, ruta_fichero):
    url = "https://www.eldoblaje.com/datos/KeywordResults.asp"
    querystring = {"keyword": keyword}
    full_url = f"{url}?{urlencode(querystring, encoding='latin1')}"

    headers = {
        "host": "www.eldoblaje.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

    response = requests.get(full_url, headers=headers)
    response.encoding = 'latin1'

    # Extraer títulos y URLs
    soup = BeautifulSoup(response.text, "html.parser")
    data = [
        {"titulo": a_tag.text.strip(), "url": f"https://www.eldoblaje.com/datos/{a_tag['href']}"}
        for td in soup.find_all("td", {"bgcolor": "#efefef"})
        if (a_tag := td.find("a", {"class": "bodyclass"}))
    ]

    # Generar el nombre del archivo si no se proporciona uno
    if not nombre_fichero:
        nombre_fichero = f"{querystring['keyword'].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    # Asegurarse de que la ruta de destino existe (para rutas absolutas o relativas)
    os.makedirs(ruta_fichero, exist_ok=True)

    # Construir la ruta completa del archivo
    ruta_completa = os.path.join(ruta_fichero, nombre_fichero)

    # Guardar los datos en un archivo JSON
    with open(ruta_completa, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    print(f"Datos guardados en el archivo: {ruta_completa}")

def mostrar_instrucciones():
    print("""
    Uso del programa:
    -------------------
    Este script busca títulos en el sitio web de Eldoblaje según una palabra clave.

    Instrucciones:
    1. Abre una terminal o consola.
    2. Navega a la carpeta donde está el ejecutable o el script.
    3. Ejecuta el siguiente comando para buscar por una palabra clave:

       python script.py -s "palabra clave" [-f NOMBRE_FICHERO] [-d RUTA_DESTINO]
    
    Ejemplo:
       python script.py -s "Harry Potter" -f resultados.json -d ./mis_datos/

    - La búsqueda se realizará en el sitio web de Eldoblaje y los resultados se guardarán en un archivo JSON.

    Opciones:
    -s, --search         Palabra clave para realizar la búsqueda.
    -f, --file           (Opcional) Nombre del archivo de salida. Por defecto, se generará un nombre único.
    -d, --directory      (Opcional) Ruta del directorio donde se guardará el archivo. Por defecto, se usará el directorio actual.
    -h, --help, -?       Muestra este mensaje de ayuda y sale.
    """)

def main():
    # Configurar argparse para aceptar los argumentos con nombre corto (-s) y largo (--search)
    parser = argparse.ArgumentParser(description="Buscar títulos por palabra clave.")
    
    # Añadir los argumentos principales
    parser.add_argument("-?", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("-s", "--search", help="Palabra clave para buscar", required=True)
    parser.add_argument("-f", "--file", help="Nombre del archivo de salida. Por defecto, se genera automáticamente.", default=None)
    parser.add_argument("-d", "--directory", help="Ruta del directorio donde se guardará el archivo. Puede ser relativa o absoluta. Por defecto, el directorio actual.", default=".")

    # Mostrar ayuda si no se pasan argumentos o si se pasa -?
    if len(sys.argv) == 1 or '-?' in sys.argv:
        parser.print_help()
        sys.exit(1)

    # Parsear los argumentos
    args = parser.parse_args()

    # Llamar a la función con los argumentos proporcionados
    obtener_y_extraer_datos(args.search, args.file, args.directory)

if __name__ == "__main__":
    main()
