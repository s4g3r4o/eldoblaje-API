# Eldoblaje API

Este proyecto es un script en Python que permite buscar y extraer información de títulos en el sitio web [Eldoblaje](https://www.eldoblaje.com). Basándose en una palabra clave proporcionada por el usuario, el script genera un archivo JSON con los títulos encontrados y sus URLs asociadas.

---

## Características

- Realiza búsquedas en el sitio web de Eldoblaje usando una palabra clave.
- Codifica la palabra clave utilizando `urlencode` con el estándar `latin1` para manejar correctamente caracteres especiales en el sitio web.
- Extrae información como el título y la URL del contenido.
- Guarda los resultados en un archivo JSON en una ruta especificada o en el directorio actual.
- Genera nombres de archivo automáticamente si no se proporciona uno.

---

## Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.7 o superior
- Librerías requeridas:
  - `argparse` (incluida por defecto en Python)
  - `sys` (incluida por defecto en Python)
  - `requests`
  - `datetime` (incluida por defecto en Python)
  - `bs4` (BeautifulSoup4)
  - `json` (incluida por defecto en Python)
  - `urllib.parse` (incluida por defecto en Python)
  - `os` (incluida por defecto en Python)

Para instalar las librerías externas, utiliza:

```bash
pip install requests beautifulsoup4
```

---

## Uso

### Ejecución del script

Para ejecutar el script, utiliza la línea de comandos:

```bash
python script.py -s "palabra clave" [-f NOMBRE_FICHERO] [-d RUTA_DESTINO]
```

### Opciones disponibles

| Argumento           | Descripción                                                                           | Obligatorio | Valor por defecto |
| ------------------- | ------------------------------------------------------------------------------------- | ----------- | ----------------- |
| `-s`, `--search`    | Palabra clave para buscar.                                                            | Sí          | N/A               |
| `-f`, `--file`      | Nombre del archivo de salida (incluye extensión .json).                               | No          | Nombre automático |
| `-d`, `--directory` | Ruta del directorio donde se guardará el archivo JSON. Puede ser relativa o absoluta. | No          | Directorio actual |
| `-h`, `-?`          | Muestra la ayuda del script.                                                          | No          | N/A               |

### Ejemplo de uso

1. Realizar una búsqueda y guardar el resultado con un nombre y ruta específicos:

```bash
python script.py -s "Harry Potter" -f resultados.json -d ./mis_datos/
```

2. Realizar una búsqueda y guardar el resultado en el directorio actual con un nombre automático:

```bash
python script.py -s "El Señor de los Anillos"
```

---

## Salida

El script genera un archivo JSON con el siguiente formato:

```json
[
    {
        "titulo": "Nombre del título",
        "url": "https://www.eldoblaje.com/url-del-titulo"
    },
    ...
]
```

El nombre del archivo puede ser personalizado o generado automáticamente. Si no se proporciona un nombre, el archivo tendrá un formato similar a este:

```
palabra_clave_YYYYMMDD_HHMMSS.json
```

Por ejemplo:

```
Harry_Potter_20250121_153000.json
```

---

## Cómo funciona el script

1. **Construcción de la URL de búsqueda:**

   - El script toma la palabra clave proporcionada por el usuario y construye una URL para realizar la búsqueda en `eldoblaje.com`.
   - Codifica correctamente la palabra clave utilizando `urlencode` con el estándar `latin1` para manejar caracteres especiales. Esto asegura que las palabras clave como "Señor de los Anillos" sean interpretadas correctamente por el sitio web.
   - Ejemplo de URL generada:
     ```
     https://www.eldoblaje.com/datos/KeywordResults.asp?keyword=Harry+Potter
     ```

2. **Obtención de los datos:**

   - Utiliza la librería `requests` para enviar una solicitud HTTP GET al sitio web.
   - Configura encabezados personalizados para evitar bloqueos.

3. **Extracción de información:**

   - Analiza el HTML obtenido con `BeautifulSoup`.
   - Busca elementos `<td>` con el atributo `bgcolor="#efefef"`.
   - Extrae el texto del título y la URL asociada de los elementos `<a>`.

4. **Guardado de los resultados:**

   - Si no se proporciona un nombre de archivo, genera uno automáticamente basado en la palabra clave y la fecha/hora actual.
   - Crea la carpeta especificada por el usuario si no existe.
   - Guarda los resultados en un archivo JSON con formato legible.

---

## Manejo de errores

El script maneja varios posibles errores:

1. **Directorio inexistente:**

   - Si el directorio especificado no existe, lo crea automáticamente.

2. **Parámetros faltantes:**

   - Si el usuario no proporciona una palabra clave, el script muestra un mensaje de ayuda.

3. **Errores de conexión:**

   - Si la conexión al sitio web falla, el script muestra un mensaje de error adecuado.

---

## Notas

- Asegúrate de tener acceso a Internet al ejecutar el script.
- Este script está diseñado específicamente para el sitio web `eldoblaje.com`. No funcionará con otros sitios sin modificaciones.
- El sitio web puede cambiar su estructura, lo que podría romper el funcionamiento del script. Si esto ocurre, deberás actualizar la lógica de extracción.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el script o reportar algún problema, crea un *issue* o envía un *pull request* en este repositorio.

---


