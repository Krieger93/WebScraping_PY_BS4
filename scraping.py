import bs4
import requests

#URL sin numero de pagina
url_base = "http://books.toscrape.com/catalogue/page-{}.html"

#Lista de titulos de libros con un rating entre 4 y 5
titulos_rating_alto = []

#Iterar paginas
for pagina in range(1,51):

    #Crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #Seleccionar datos de los libros de cada pagina
    libros = sopa.select('.product_pod')

    #Iterar por cada libro de cada pagina
    for libro in libros:

        #check que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            #Guardar titulo en variable
            titulos_rating_alto.append(libro.select('a')[1]['title'])


for t in titulos_rating_alto:
    print(t)
