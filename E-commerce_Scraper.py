from bs4 import BeautifulSoup
import pandas as pd
import requests

#PARA SOLICITAR UN NUMERO LIMITADO DE PAGINAS DE LA PLATAFORMA

"""datos_libros = []

# Definimos cuántas páginas queremos recorrer (ej. del 1 al 5)
total_paginas = 5

for pagina in range(1, total_paginas + 1):
  # Construimos la URL dinámica para cada página
  url = f'http://books.toscrape.com/catalogue/page-{pagina}.html'
  print(f'Extrayendo datos de la página {pagina}...')

  response = requests.get(url)
  response.encoding = 'utf-8'

  # Si la página existe (código 200), extraemos los datos
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    libros = soup.find_all('article', class_='product_pod')

    for libro in libros:
      titulo = libro.h3.a['title']
      precio_str = (
          libro.find('p', class_='price_color').text.strip().replace('£', '')
      )
      precio = float(precio_str)
      disponibilidad = (
          libro.find('p', class_='instock availability').text.strip()
      )

      datos_libros.append({
          'Pagina': pagina,
          'Titulo': titulo,
          'Precio': precio,
          'Disponibilidad': disponibilidad,
      })
  else:
    print(f'No se pudo acceder a la página {pagina}')
    break
    """


########################################################################################################
# EN CASO DE QUERER TOMAR TODAS LAS PAGINAS DE LA PLATAFORMA

datos_libros = []
pagina = 1

while True:
  url = f'http://books.toscrape.com/catalogue/page-{pagina}.html'
  print(f'Extrayendo datos de la página {pagina}...')

  response = requests.get(url)

  # Si la página ya no existe (error 404), rompemos el ciclo y terminamos
  if response.status_code != 200:
    print('Se han agotado las páginas disponibles.')
    break

  response.encoding = 'utf-8'
  soup = BeautifulSoup(response.text, 'html.parser')
  libros = soup.find_all('article', class_='product_pod')

  for libro in libros:
    titulo = libro.h3.a['title']
    precio_str = (
        libro.find('p', class_='price_color').text.strip().replace('£', '')
    )
    precio = float(precio_str)
    disponibilidad = libro.find('p', class_='instock availability').text.strip()

    datos_libros.append({
        'Pagina': pagina,
        'Titulo': titulo,
        'Precio_Libras': precio,
        'Disponibilidad': disponibilidad,
    })

  # Incrementamos el número de página para la siguiente iteración
  pagina += 1 

# Convertimos todo el acumulado en un DataFrame de Pandas
df = pd.DataFrame(datos_libros)

# Exportamos el resultado completo a Excel
archivo_salida = 'libros_extraidos.xlsx'
df.to_excel(archivo_salida, index=False)

print(
    f'¡Proceso terminado! Se guardaron en {archivo_salida}'
)