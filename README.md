# 🕷️ Web Scraper Automatizado de E-commerce con Python, BeautifulSoup y Pandas

Repositorio enfocado en demostrar habilidades de **Ingeniería de Datos y Automatización Web**, extrayendo catálogos masivos de comercio electrónico de forma estructurada y exportándolos a formatos analíticos limpios.

---

## 🎯 Objetivo Principal
Automatizar la extracción de datos de productos (títulos, precios y disponibilidad) desde un sitio web de comercio electrónico simulado, implementando control de paginación dinámica y transformando texto sin formato en un dataset estructurado apto para análisis o bases de datos.

El script cuenta con dos modalidades configurables:
1. **Extracción limitada:** Recorre un rango específico de páginas definido por el usuario.
2. **Extracción masiva automatizada (`while True`):** Navega dinámicamente por todo el catálogo hasta detectar el fin de las páginas mediante códigos de estado HTTP (`404`), asegurando robustez y escalabilidad.

---

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python:** Lenguaje principal de programación.
* **Requests:** Realización de peticiones HTTP para la obtención del código fuente HTML.
* **BeautifulSoup (bs4):** Parseo, análisis y extracción selectiva de elementos del DOM.
* **Pandas:** Estructuración de datos tabulares y exportación a Excel.
* **OpenPyXL:** Motor subyacente para la escritura de archivos .xlsx.

---

## 🚀 Cómo Ejecutar el Proyecto
Clona este repositorio en tu computadora.
Abre tu terminal en la carpeta del proyecto e instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

Ejecuta el script principal de Python:

```bash
python E-commerce_Scraper.py
```
Al finalizar, se generará de manera automática el archivo libros_extraidos.xlsx listo para su uso.

## 🔄 Funcionamiento del Código
* **Control de Errores HTTP:** Valida el estatus de la respuesta del servidor (status_code == 200) antes de procesar cualquier página para evitar caídas inesperadas.
* **Limpieza en Tiempo de Ejecución:** Realiza transformaciones clave al vuelo, como limpiar símbolos monetarios (£), convertir los precios de texto a números flotantes (float) y eliminar espacios sobrantes con .strip().
* **Trazabilidad:** Agrega una columna de control (Pagina) para identificar exactamente el origen de cada registro extraído.
